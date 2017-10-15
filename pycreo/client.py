from pycreo.commands import (
    ConnectionCommandsMixin,
    CreoCommandsMixin,
    DimensionCommandsMixin,
    FileCommandsMixin,
    ParameterCommandsMixin,
    GeometryCommandsMixin
)
from pycreo.core import CreosonApi
from pycreo import configs
from pycreo.http_client import HttpClient


class CreosonClient(ConnectionCommandsMixin,
                    CreoCommandsMixin,
                    DimensionCommandsMixin,
                    FileCommandsMixin,
                    ParameterCommandsMixin,
                    GeometryCommandsMixin,
                    CreosonApi):
    _configs = configs.configs

    def __init__(self):
        super().__init__(
            api_url=self._configs.get('API_URL'),
            http_client=HttpClient()
        )

    @property
    def configs(self):
        return self._configs

    @property
    def api_url(self):
        return self.http_client.api_url
