from __future__ import absolute_import

import os
import re
import string

from .pinboard import Pinboard


SAFE_CHARACTERS = (string.ascii_letters + string.digits + '-_.() ')


def export(auth_token, path=None):
    pb = Pinboard(auth_token)

    bookmarks = pb.bookmarks()

    for bookmark in bookmarks:
        filename = bookmark['description']
        filename = re.sub(r'[\s\n\r]+', " ", filename)
        filename = ''.join(filter(lambda x: x in SAFE_CHARACTERS, filename))

        if not filename:
            continue

        tags = bookmark['tags']
        tags = list(filter(lambda x: x in SAFE_CHARACTERS, tags))
        tags = f' [{tags}]'

        filename = filename[:210 - len(tags)]
        filename += tags
        filename = filename.strip()
        filename += ".url"

        if path:
            os.chdir(path)

        with open(filename, 'w') as f:
            f.write(f"[InternetShortcut]\r\nURL={bookmark['href']}")
