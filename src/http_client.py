import abc

import requests

r_session = requests.Session()


class AbstractHttpClient(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_api_url(self, api_url):
        pass

    @abc.abstractmethod
    def send_request(self, data):
        pass


class HttpClient(AbstractHttpClient):
    def __init__(self):
        self.session = r_session
        self.api_url = None

    def set_api_url(self, api_url):
        self.api_url = api_url

    def send_request(self, data):
        resp = self.session.post(self.api_url, json=data)
        return resp.json()
