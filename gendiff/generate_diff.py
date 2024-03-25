#!/usr/bin/env python3
import json
import yaml
import os
import sys
from gendiff.stylish import formatter


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
    def for_nested(first_dict, second_dict):
        result = []
        keys1, keys2 = first_dict.keys(), second_dict.keys()
        all_keys = keys1 | keys2
        for key in sorted(all_keys):
            if key not in keys1:
                step_result = {
                    'name': key,
                    'status': 'added',
                    'what_added': second_dict[key]
                }
                result.append(step_result)
            elif key not in keys2:
                step_result = {
                    'name': key,
                    'status': 'deleted',
                    'what_deleted': first_dict[key]
                }
                result.append(step_result)
            elif first_dict[key] == second_dict[key]:
                step_result = {
                    'name': key,
                    'status': 'unchanged',
                    'intact': first_dict[key]
                }
                result.append(step_result)
            else:
                if isinstance(first_dict[key], dict) and isinstance(second_dict[key], dict):
                    step_result = {
                        'name': key,
                        'status': 'nested',
                        'children': for_nested(first_dict[key], second_dict[key])
                    }
                    result.append(step_result)
                else:
                    step_result = {
                        'name': key,
                        'status': 'changed',
                        'from_first_dict': first_dict[key],
                        'from_second_dict': second_dict[key]
                    }
                    result.append(step_result)
        return result
    diff = sorted(for_nested(file1, file2), key=lambda x: x['name'])
    return formatter(diff)

