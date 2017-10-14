from src.commands import ConnectionCommandsMixin
from src.core import CreosonApi
from src import configs
from src.http_client import HttpClient


class CreosonClient(ConnectionCommandsMixin,
                    CreosonApi):
    def __init__(self):
        super().__init__(api_url=configs.API_URL, http_client=HttpClient())

    @property
    def api_url(self):
        return self.http_client.api_url
