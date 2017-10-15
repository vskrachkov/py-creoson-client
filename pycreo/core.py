class CreosonApi:
    def __init__(self, api_url, http_client):
        self.http_client = http_client
        self.http_client.set_api_url(api_url)
