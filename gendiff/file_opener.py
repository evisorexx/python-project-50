import json
import yaml
import os
import sys


def check_file_format(path):
    if path.endswith('.yml') or path.endswith('.yaml'):
        return 'YAML'
    elif path.endswith('.json'):
        return 'JSON'
    else:
        return 'UNKNOWN'


def file_opening(path):
    try:
        _ = open(path)
    except FileNotFoundError:
        print("The file doesn't exist.")
        sys.exit()
    if os.stat(path).st_size == 0:
        return {}
    match check_file_format(path):
        case 'JSON':
            return json.load(open(path, 'r'))
        case 'YAML':
            return yaml.load(open(path, 'r'), Loader=yaml.SafeLoader)
        case 'UNKNOWN':
            print('Unknown format of file!')
            sys.exit(0)
