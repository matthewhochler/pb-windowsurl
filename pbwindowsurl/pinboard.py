import json
import urllib
import urllib2


def url_with_params(url, params):
    return url + "?" + urllib.urlencode(params)


class PinboardError(Exception):
    pass


class Pinboard(object):
    BASE_URL = "https://api.pinboard.in/v1"
    OK_CODE = 200

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def call(self, resource_path, params=None):
        req_params = {
            'auth_token': self.auth_token,
            'format': 'json',
        }

        if params:
            req_params.update(params)

        req_url = "{base_url}{resource_path}".format(
            base_url=self.BASE_URL,
            resource_path=resource_path,
        )

        resp = urllib2.urlopen(url_with_params(req_url, req_params))

        if resp.code != self.OK_CODE:
            raise PinboardError(resp.msg)

        return json.loads(resp.read())

    def bookmarks(self):
        return self.call("/posts/all")
