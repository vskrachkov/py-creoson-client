
class CreosonApi:
    def __init__(self, api_url, http_client):
        self.http_client = http_client
        self.http_client.set_api_url(api_url)

    def connect(self):
        resp = self.http_client.send_request(data={
            'command': 'connection',
            'function': 'connect',
        })
        session_id = resp.get('sessionId')
        return session_id

    def disconnect(self, session_id):
        resp = self.http_client.send_request(data={
            'command': 'connection',
            'function': 'disconnect',
            'sessionId': session_id
        })
        return resp
