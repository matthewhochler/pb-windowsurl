from __future__ import absolute_import

import re
import string

from .pinboard import Pinboard


def export(auth_token, path=None):
    pb = Pinboard(auth_token)

    bookmarks = pb.bookmarks()

    x = 0
    for bookmark in bookmarks:
        x += 1

        filename = re.sub(r'[\s\n\r]+', " ", bookmark['description'])
        filename = filter(lambda x: x in string.printable, filename)
        filename = filename[:250]
        filename += ".url"

        if path:
            if not path.endswith("\\"):
                path += "\\"

            filename = path + filename

        with open(filename, 'wb') as f:
            print filename
            f.write("[InternetShortcut]\r\nURL=" + bookmark['href'])

        if x > 10:
            break
