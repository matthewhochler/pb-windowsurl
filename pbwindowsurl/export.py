from __future__ import absolute_import

import platform
import re
import string

from .pinboard import Pinboard


def export(auth_token, path=None):
    pb = Pinboard(auth_token)

    bookmarks = pb.bookmarks()

    for bookmark in bookmarks:
        filename = re.sub(r'[\s\n\r]+', " ", bookmark['description'])
        filename = filter(
            lambda x: x in (string.ascii_letters + string.digits + "-_.() "),
            filename,
        )
        filename = filename[:200]

        if not filename:
            continue

        filename += ".url"

        if path:
            if platform.system() == "Windows":
                if not path.endswith("\\"):
                    path += "\\"
            else:
                if not path.endswith("/"):
                    path += "/"

            filename = path + filename

        with open(filename, 'wb') as f:
            f.write("[InternetShortcut]\r\nURL=" + bookmark['href'])
