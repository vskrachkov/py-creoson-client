import os

configs = {
    # url on which creoson server is running
    'API_URL': os.getenv('PY_CREOSON_API_URL', 'http://192.168.0.104:9056/creoson'),

    # directory that contains .bat file with instructions to run Creo
    'START_DIR': os.getenv('PY_CREOSON_START_DIR', 'C:\\Program Files\\PTC'),

    # name of the .bat file with instructions to run Creo
    'START_FILE_NAME': os.getenv('PY_CREOSON_START_FILE', 'nitro_proe_remote.bat'),

    # number of retries to make when connecting to Creo
    # the server will pause for 3 seconds between connection retries
    'CONNECTING_RETRIES': os.getenv('PY_CREO_RETRIES', 0)
}
