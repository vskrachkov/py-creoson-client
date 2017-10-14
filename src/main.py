from src import configs
from src.core import CreosonApi
from src.http_client import HttpClient


if __name__ == '__main__':
    api = CreosonApi(api_url=configs.API_URL, http_client=HttpClient())
    print(f'api url: {configs.API_URL}')

    print('getting session id')
    session_id = api.connect()
    print(f'session id: {session_id}')

    print('closing session')
    resp = api.disconnect(session_id)
    print(f'disconnect response {resp}')
