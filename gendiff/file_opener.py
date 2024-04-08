import json
import yaml
import os
import sys


def check_file_format(path):
    if path.endswith('.yml') or path.endswith('.yaml'):
        return yaml.load(open(path, 'r'), Loader=yaml.SafeLoader)
    elif path.endswith('.json'):
        return json.load(open(path, 'r'))
    else:
        print('Unknown format of file!')
        sys.exit(0)


def file_opening(path):
    try:
        _ = open(path)
    except FileNotFoundError:
        print("The file doesn't exist.")
        sys.exit()
    if os.stat(path).st_size == 0:
        return {}
    else:
        return check_file_format(path)
