class ConnectionCommandsMixin:
    def connect(self):
        resp = self.http_client.send_request({
            'command': 'connection',
            'function': 'connect',
        })
        session_id = resp.get('sessionId')
        return session_id

    def disconnect(self, session_id):
        resp = self.http_client.send_request({
            'command': 'connection',
            'function': 'disconnect',
            'sessionId': session_id
        })
        return resp
