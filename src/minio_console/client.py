import requests
import json

class MinioConsoleClient:
    def __init__(self, url, username, password):
        # docs: https://github.com/minio/console/blob/master/swagger-console.yml
        self.url = url + "/api/v1"
        self.username = username
        self.password = password
        self.token = self._login()
        self.headers = {
            'Content-Type': 'application/json',
            'Cookie': self.token,
        }

    def _login(self):
        payload = {
            'accessKey': self.username,
            'secretKey': self.password
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.url + "/login", headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.headers.get("set-cookie").split(";")[0]

    def _do(self, method, path, params=None, data=None):
        response = requests.request(method, self.url + path, params=params, data=data, headers=self.headers)
        response.raise_for_status()
        return response

    def get(self, path, params=None, data=None):
        return self._do("GET", path, params=params, data=data)

    def delete(self, path, params=None, data=None):
        return self._do("DELETE", path, params=params, data=data)

    def post(self, path, params=None, data=None):
        return self._do("POST", path, params=params, data=data)

    def put(self, path, params=None, data=None):
        return self._do("PUT", path, params=params, data=data)


class MinioBaseResource:
    def __init__(self, client):
        self.client = client