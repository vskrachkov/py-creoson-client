# py-creoson-client
Python client for creoson library (http://www.creoson.com)

# Example of usage:

#### Configuration
For correct work you must define some environment variable
on machine where python client is installed.

- `PY_CREOSON_API_URL` -> url on which the creoson server is running
    (default: http://192.168.0.104:9056/creoson);
- `PY_CREOSON_START_DIR` -> directory that contains .bat file with instructions to run Creo
    (default: 'C:\\\\Program Files\\\\PTC');
- `PY_CREOSON_START_FILE` -> name of the .bat file with instructions to run Creo
    (default: 'nitro_proe_remote.bat');
- `PY_CREO_RETRIES` -> number of retries to make when connecting to Creo.
    The server will pause for 3 seconds between connection retries
    (default: 0);
- `PY_CREO_WORK_DIR` -> path to the work directory with creo project
    (default: 'c:\\\\').

If you on unix based os than you can set variables in this way:
```
export PY_CREOSON_API_URL=http://192.168.0.104:9056/creoson;
export PY_CREOSON_START_DIR=C:\\\\Program\ Files\\\\PTC;
export PY_CREOSON_START_FILE=nitro_proe_remote.bat;
export PY_CREO_RETRIES=0;
export PY_CREO_WORK_DIR=c:\\\\;
```

#### Initializing of creoson client and getting session id.
code:
```
client = CreosonClient()
print(f'api url: {client.api_url}')

print('getting session id ...')
session_id, err = client.connect()
print(f'session id: {session_id}')

print('check that creo is running ...')
is_running, err = client.is_creo_running()
print(f'is creo running: {is_running}')
```
result:
```
api url: http://192.168.0.100:9056/creoson
getting session id ...
session id: -1841284680323710244
check that creo is running ...
is creo running: True
```
Save session after retrieving, do not reconnect
to server each time when you want execute command.

#### Go to the working directory (PY_CREO_WORK_DIR)
code:
```
print('go to the working dir ...')
    curr_dir, err = client.go_to_work_dir(session_id)
    print(f'go to the working dir resp: {curr_dir}')
```
result:
```
go to the working dir ...
go to the working dir resp: e:/creo_project
```

#### Getting current directory
code:
```
print('getting current directory ...')
curr_dir, err = client.pwd(session_id)
print(f'curr dir {curr_dir}')
```
result:
```
getting current directory ...
curr dir e:/creo_project/
```

#### List of the directories in current directory
code:
```
print('creo list_dirs ...')
dirlist, err = client.dir_list(session_id)
print(f'list_dir resp: {dirlist}')
```
result:
```
creo list_dirs ...
list_dir resp: ['step', 'other_dir']
```

#### List of the files in current directory
code:
```
print('list files ...')
filelist, err = client.files_list(session_id)
print(f'files list: {filelist}')
```
result:
```
list files ...
files list: ['center_block.prt', 'coller.prt', 'fork.prt', 'key1.prt', 'pin.prt', 'shaft1.prt', 'taper_pin.prt', 'universal_coupling.asm']
```

#### Create and remove directory
code:
```
print('create temp dir ...')
    resp, err = client.mkdir(session_id, dirname='temp')

print('remove temp dir')
resp, err = client.rmdir(session_id, dirname='temp')
print(f'remove response: {resp}')
```
result:
```
create temp dir ...
remove temp dir
remove response: {'status': {'error': False}}
```

#### Opening files
open multiple files:
```
resp, err = client.open_files(
    session_id,
    dirname=curr_dir,
    filenames=('universal_coupling.asm',
               'key1.prt',
               'pin.prt',
               'cooler.prt', )
)
```
open single file:
```
resp, err = client.open_file(session_id, dirname=curr_dir, filename='pin.prt')
```

#### Getting list of model dimensions
Take in mind that file must be previously open

code:
```
dimlist, err = client.dimensions_list(session_id, filename='fork.prt')
```
result:
```
[
    {'name': 'd0', 'value': 84.0, 'encoded': False},
    {'name': 'd1', 'value': 16.0, 'encoded': False},
    {'name': 'd2', 'value': 40.0, 'encoded': False},
    {'name': 'd3', 'value': 18.0, 'encoded': False},
    {'name': 'd4', 'value': 57.0, 'encoded': False},
     ...
    {'name': 'd20', 'value': 3.5, 'encoded': False}
]
```

#### Getting list of model parameters
code:
```
paramlist, err = client.parameters_list(session_id, filename='fork.prt')
```
result:
```
[
    {'owner_name': 'fork.prt', 'designate': True, 'name': 'DESCRIPTION', 'type': 'STRING', 'value': '', 'encoded': False},
    {'owner_name': 'fork.prt', 'designate': True, 'name': 'MODELED_BY', 'type': 'STRING', 'value': '', 'encoded': False}
]
```

#### Getting bound box of the model
code:
```
resp, err = client.bound_box(session_id, filename='fork.prt')
```
result:
```
{
    'ymax': 42.0,
    'zmin': -28.5,
    'xmax': 20.018745325575885,
    'ymin': -42.0,
    'xmin': -72.0,
    'zmax': 28.5
}
```

#### Getting list of surfaces
code:
```
surfaces, err = client.get_surfaces(session_id, filename='coller.prt')
```
result:
```
[
    {'area': 289.81192229365803, 'min_extent': {'x': -12.5, 'z': -12.5, 'y': -5.0}, 'max_extent': {'x': 12.5, 'z': 12.5, 'y': -5.0}, 'surface_id': 43},
    {'area': 289.81192229365803, 'min_extent': {'x': -12.5, 'z': -12.5, 'y': 5.0}, 'max_extent': {'x': 12.5, 'z': 12.5, 'y': 5.0}, 'surface_id': 48},
    {'area': 385.6179835229232, 'min_extent': {'x': -12.5, 'z': -12.5, 'y': -5.0}, 'max_extent': {'x': 12.5, 'z': 0.0, 'y': 5.0}, 'surface_id': 53},
     ...
    {'area': 42.653328805498475, 'min_extent': {'x': -1.5, 'z': -12.500000105392925, 'y': -1.5}, 'max_extent': {'x': 1.5, 'z': 12.500000187907663, 'y': 1.8369701987210297e-16}, 'surface_id': 81}
]
```

#### Getting surface ids list of the model
code:
```
surface_ids, err = client.get_surface_ids(session_id, filename='coller.prt')
```
result:
```
(43, 48, 53, 55, 57, 59, 79, 81)
```

#### Getting list of the model edges grouped by contours
code:
```

```
result:
```
[
    {
        'traversal': 'external',
        'edgelist': [
            {
                'end': {'x': -12.5, 'z': -1.5308084989341915e-15, 'y': -5.0},
                'edge_id': 44,
                'length': 39.26990816987246,
                'start': {'x': 12.5, 'z': 1.5308084989341921e-15, 'y': -5.0}
            },
            {
                'end': {'x': 12.5, 'z': 1.5308084989341921e-15, 'y': -5.0},
                'edge_id': 45,
                'length': 39.26990816987245,
                'start': {'x': -12.5, 'z': -1.5308084989341915e-15, 'y': -5.0}
            }
        ],
    'surface_id': 43},
    {
        'traversal': 'internal',
        'edgelist': [
            {
                'end': {'x': -8.0, 'z': -9.797174393178826e-16, 'y': -5.0},
                'edge_id': 46,
                'length': 25.132741228718334,
                'start': {'x': 8.0, 'z': 9.797174393178871e-16, 'y': -5.0}
            },
            {
                'end': {'x': 8.0, 'z': 9.797174393178871e-16, 'y': -5.0},
                'edge_id': 47, 'length': 25.13274122871835,
                'start': {'x': -8.0, 'z': -9.797174393178826e-16, 'y': -5.0}
            }
        ],
    'surface_id': 43},
    ...
]
```

#### Getting paths to the parts in the assembly
code:
```
children, err = client.get_paths(
    session_id,
    filename='universal_coupling.asm',
    paths=True,
    skeletons=True,
)
```
result:
```
{
    'children': [{'file': 'FORK.PRT', 'path': [40], 'seq_path': 'root.1'},
                 {'file': 'CENTER_BLOCK.PRT', 'path': [41], 'seq_path': 'root.2'},
                 {'file': 'PIN.PRT', 'path': [46], 'seq_path': 'root.3'},
                 {'file': 'COLLER.PRT', 'path': [48], 'seq_path': 'root.4'}],
     'file': 'universal_coupling.asm',
     'seq_path': 'root'
}
```

#### Closing the Creo
```
print('stopping creo')
if is_running:
    resp, err = client.stop_creo(session_id)
    if err:
        print(f'stop with error, detail: {resp}')
    else:
        print('creo is stopped')
```

#### Starting the Creo
```
resp, err = client.start_creo()
if err:
    print(f'error: {err}, resp: {resp}')
else:
    print('creo is started')
```