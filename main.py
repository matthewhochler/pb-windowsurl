import os
import sys

from pbwindowsurl import export


if __name__ == '__main__':
    auth_token = sys.argv[1]

    try:
        path = sys.argv[2]
    except IndexError:
        path = os.getcwd()

    export.export(auth_token, path)
