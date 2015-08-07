from pbwindowsurl import export


def main(auth_token, path):
    export.export(auth_token, path)


if __name__ == '__main__':
    import os
    import sys

    auth_token = sys.argv[1]

    try:
        path = sys.argv[2]
    except IndexError:
        path = os.getcwd()

    main(auth_token, path)
