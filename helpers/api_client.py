import requests
from data import Data

class APIClient:
    def __init__(self):
        self.base_url = Data.URL
        self.timeout = 3

    def post(self, endpoint, data=None, json=None):
        return requests.post(f"{self.base_url}{endpoint}", data=data, json=json, timeout=self.timeout)

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params, timeout=self.timeout)

    def put(self, endpoint, params=None):
        return requests.put(f"{self.base_url}{endpoint}", params=params, timeout=self.timeout)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}", timeout=self.timeout)
