"""
commands.py

Each command returns tuple with two elements:
    - command error (True if error is occurred or False if not)
    - command response data

"""


class BaseCommandMixin:
    def _send_request(self, data):
        resp = self.http_client.send_request(data)
        error = resp['status']['error']
        return resp, error


class ConnectionCommandsMixin(BaseCommandMixin):
    def connect(self):
        """Returns connection sessionId."""
        resp, err = self._send_request({
            'command': 'connection',
            'function': 'connect',
        })

        session_id = resp.get('sessionId')
        return session_id, err

    def disconnect(self, session_id):
        resp, err = self._send_request({
            'command': 'connection',
            'function': 'disconnect',
            'sessionId': session_id
        })
        return resp, err

    def is_creo_running(self):
        resp, err = self._send_request({
            'command': 'connection',
            'function': 'is_creo_running',
        })
        data = resp.get('data')
        if data:
            return data.get('running'), err

    def start_creo(self):
        resp, err = self._send_request({
            'command': 'connection',
            'function': 'start_creo',
            'data': {
                'start_dir': self._configs.get('START_DIR'),
                'start_command': self._configs.get('START_FILE_NAME'),
                'retries': self._configs.get('CONNECTING_RETRIES')
            }
        })

        return resp, err

    def stop_creo(self, session_id):
        resp, err = self._send_request({
            'command': 'connection',
            'function': 'stop_creo',
            'sessionId': session_id
        })
        return resp, err


class CreoCommandsMixin(BaseCommandMixin):
    def dir_list(self, session_id):
        resp, err = self._send_request({
            'command': 'creo',
            'function': 'list_dirs',
            'sessionId': session_id,
            'data': {
                'dirname': '*'
            }
        })
        return resp, err
