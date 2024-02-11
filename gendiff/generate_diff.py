#!/usr/bin/env python3
import json
import yaml
import os
import sys


def values_format(item):
    if item is True:
        return 'true'
    if item is False:
        return 'false'
    return item


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


def generate_diff(path1, path2):
    file1, file2 = format_opening(path1), format_opening(path2)

    items1 = sorted(file1.items())
    items2 = sorted(file2.items())
    output = '{\n'

    for item in items1:
        if file2.get(item[0]) is not None:
            if file1[item[0]] == file2[item[0]]:
                output += f'    {item[0]}: {values_format(item[1])}\n'
            else:
                output += f'  - {item[0]}: {values_format(item[1])}\n'
                output += f'  + {item[0]}: {values_format(file2[item[0]])}\n'
        else:
            output += f'  - {item[0]}: {values_format(item[1])}\n'

    for item in items2:
        if file1.get(item[0]) is None:
            output += f'  + {item[0]}: {values_format(item[1])}\n'

    return output + '}'
