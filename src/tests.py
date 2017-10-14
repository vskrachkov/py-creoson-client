from src.client import CreosonClient


if __name__ == '__main__':
    client = CreosonClient()
    print(f'api url: {client.api_url}')

    print('getting session id')
    session_id = client.connect()
    print(f'session id: {session_id}')

    print('closing session')
    resp = client.disconnect(session_id)
    print(f'disconnect response {resp}')
