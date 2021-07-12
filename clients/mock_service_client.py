import time
import uuid

# In-Memory Cache
libraries = []


def load_libraries() -> []:
    time.sleep(0.5)
    return libraries


def add_library(dir_type: str, dir_path: str) -> object:
    time.sleep(0.5)
    for library in libraries:
        if library['path'].startswith(dir_path):
            raise Exception('Directory or its parent/child directory is already registered.')
    library = {'id': str(uuid.uuid4()), 'type': dir_type, 'path': dir_path}
    libraries.append(library)
    return library


def remove_library(lib_id: str):
    time.sleep(0.5)
    for d in libraries:
        if d['id'] == lib_id:
            libraries.remove(d)
            break


def rescan_library(lib_id: str):
    time.sleep(0.5)
    pass
