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
    def dir_list(self, session_id, dirname_mask=None):
        resp, err = self._send_request({
            'command': 'creo',
            'function': 'list_dirs',
            'sessionId': session_id,
            'data': {
                'dirname': dirname_mask or '*'
            }
        })
        return resp, err

    def files_list(self, session_id, dirname_mask=None, filename_mask=None):
        resp, err = self._send_request({
            'command': 'creo',
            'function': 'list_files',
            'sessionId': session_id,
            'data': {
                'dirname': dirname_mask or '*',
                'filename': filename_mask or '*'
            }
        })
        return resp, err

    def go_to_work_dir(self, session_id):
        return self.cd(session_id, self._configs.get('WORK_DIR'))

    def cd(self, session_id, dirname):
        resp, err = self._send_request({
            'command': 'creo',
            'function': 'cd',
            'sessionId': session_id,
            'data': {
                'dirname': dirname
            }
        })
        return resp, err

    def mkdir(self, session_id, dirname):
        resp, err = self._send_request({
            'command': 'creo',
            'function': 'mkdir',
            'sessionId': session_id,
            'data': {
                'dirname': dirname
            }
        })
        return resp, err

    def pwd(self, session_id):
        """Returns path to the current directory."""
        resp, err = self._send_request({
            'command': 'creo',
            'function': 'pwd',
            'sessionId': session_id,
        })
        curr_dir = resp['data']['dirname']
        return curr_dir, err

    def rmdir(self, session_id, dirname):
        """Removes empty directory."""
        resp, err = self._send_request({
            'command': 'creo',
            'function': 'mkdir',
            'sessionId': session_id,
            'data': {
                'dirname': dirname
            }
        })
        return resp, err


class DimensionCommandsMixin(BaseCommandMixin):
    def dimensions_list(self, session_id, filename, dimension_names=()):
        resp, err = self._send_request({
            'command': 'dimension',
            'function': 'list',
            'sessionId': session_id,
            'data': {
                'file': filename,
                'names': dimension_names
            }
        })
        return resp, err


class FileCommandsMixin(BaseCommandMixin):
    def open_file(self,
                  session_id,
                  dirname,
                  filenames=(),
                  display=False,
                  activate=False,
                  new_window=False,
                  regen_force=False):
        resp, err = self._send_request({
            'command': 'file',
            'function': 'open',
            'sessionId': session_id,
            'data': {
                'dirname': dirname,
                'files': filenames,
                'display': display,
                'activate': activate,
                'new_window': new_window,
                'regen_force': regen_force,
            }
        })
        return resp, err


class ParameterCommandsMixin(BaseCommandMixin):
    def parameters_list(self,
                        session_id,
                        filename=None,
                        parameters=(),
                        value_filter=''):
        resp, err = self._send_request({
            'command': 'parameter',
            'function': 'list',
            'sessionId': session_id,
            'data': {
                'file': filename,
                'names': parameters,
                'value': value_filter,
            }
        })
        return resp, err


class GeometryCommandsMixin(BaseCommandMixin):
    def bound_box(self, session_id, filename):
        resp, err = self._send_request({
            'command': 'geometry',
            'function': 'bound_box',
            'sessionId': session_id,
            'data': {
                'file': filename,
            }
        })
        return resp, err

    def get_edges(self, session_id, surface_ids, filename=None):
        resp, err = self._send_request({
            'command': 'geometry',
            'function': 'get_edges',
            'sessionId': session_id,
            'data': {
                'file': filename,
                'surface_ids': surface_ids
            }
        })
        contourlist = resp['data']['contourlist']
        return contourlist, err

    def get_surfaces(self, session_id, filename):
        resp, err = self._send_request({
            'command': 'geometry',
            'function': 'get_surfaces',
            'sessionId': session_id,
            'data': {
                'file': filename,
            }
        })
        surflist = resp['data']['surflist']
        return surflist, err
