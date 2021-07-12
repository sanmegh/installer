import json

import requests

# Service endpoints
DIRECTORIES_ENDPOINT = 'http://192.168.1.107:8088/driveman-server/directories'

# Error messages
CONNECTION_ERROR = 'Failed to connect! Please ensure that the server is up and running.'


def __extract_error(response) -> str:
    full_error_msg: str = json.loads(response.text)['message']
    error_msg = full_error_msg[full_error_msg.rfind(':') + 2:]
    return error_msg


def load_libraries() -> []:
    try:
        response = requests.get(DIRECTORIES_ENDPOINT)
    except Exception as e:
        raise Exception(CONNECTION_ERROR)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(__extract_error(response))


def add_library(dir_type: str, dir_path: str):
    request_body = {'type': dir_type, 'path': dir_path}
    try:
        response = requests.post(url=DIRECTORIES_ENDPOINT, json=request_body)
    except Exception as e:
        raise Exception(CONNECTION_ERROR)
    if response.status_code != 200:
        raise Exception(__extract_error(response))


def remove_library(directory_id: str):
    try:
        response = requests.delete(DIRECTORIES_ENDPOINT + '/' + directory_id)
    except Exception as e:
        raise Exception(CONNECTION_ERROR)
    if response.status_code != 200:
        raise Exception(__extract_error(response))


def rescan_library(directory_id: str):
    try:
        response = requests.put(DIRECTORIES_ENDPOINT + '/' + directory_id)
    except Exception as e:
        raise Exception(CONNECTION_ERROR)
    if response.status_code != 200:
        raise Exception(__extract_error(response))
