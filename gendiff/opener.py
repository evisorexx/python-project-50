#!/usr/bin/env python3
import json
import yaml
import os
import sys


def format_opening(path):
    # Checking for existence of file
    try:
        _ = open(path)
    except FileNotFoundError:
        print("The file doesn't exist.")
        sys.exit()
    # Checking for emptiness of file
    if os.stat(path).st_size == 0:
        return {}
    # Checking for format of file
    if path.endswith('.yml') or path.endswith('.yaml'):
        opened_file = yaml.load(open(path, 'r'), Loader=yaml.SafeLoader)
    elif path.endswith('.json'):
        opened_file = json.load(open(path, 'r'))
    else:
        print('Unknown format of file!')
        sys.exit(0)

    return opened_file
