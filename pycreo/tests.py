from pycreo import CreosonClient


if __name__ == '__main__':
    client = CreosonClient()
    print(f'api url: {client.api_url}')

    print('getting session id ...')
    session_id, err = client.connect()
    print(f'session id: {session_id}')

    print('check that creo is running ...')
    is_running, err = client.is_creo_running()
    print(f'is creo running: {is_running}')

    # print('creo list_dirs ... ')
    # resp, err = client.dir_list(session_id)
    # print(f'list_dir resp: {resp}')

    print('go to the working dir ...')
    resp, err = client.go_to_work_dir(session_id)

    print('creo list_dirs ...')
    resp, err = client.dir_list(session_id)
    print(f'list_dir resp: {resp}')

    print('list files ...')
    resp, err = client.files_list(session_id)
    print(f'files list: {resp}')

    # print('create temp dir ...')
    # resp, err = client.mkdir(session_id, dirname='temp')
    #
    # print('creo list_dirs')
    # resp, err = client.dir_list(session_id)
    # print(f'list_dir resp: {resp}')

    print('getting current work directory ...')
    curr_dir, err = client.pwd(session_id)
    print(f'curr dir {resp}')
    #
    # print('removing directory')
    # resp, err = client.rmdir(session_id, 'temp')

    # print('creo list_dirs')
    # resp, err = client.dir_list(session_id)
    # print(f'list_dir resp: {resp}')

    print('opening the file ...')
    resp, err = client.open_file(session_id, dirname=curr_dir, filenames=('Fork.prt', ), display=True)
    print(f'open resp: {resp}')

    print('getting dimensions')
    resp, err = client.dimensions_list(session_id, filename='fork.prt')
    print(f'dimensions list: {resp}')

    print('getting parameters list ...')
    resp, err = client.parameters_list(session_id, filename='fork.prt')
    print(f'parameters list: {resp}')

    # print('stopping creo')
    # if is_running:
    #     resp, err = client.stop_creo(session_id)
    #     if err:
    #         print(f'stop with error, detail: {resp}')
    #     else:
    #         print('creo is stopped')

    # print('starting creo')
    # resp, err = client.start_creo()
    # if err:
    #     print(f'error: {err}, resp: {resp}')
    # else:
    #     print('creo is started')

    print('closing session')
    _, err = client.disconnect(session_id)
    print(f'error during disconnect: {err}')
