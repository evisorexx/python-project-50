#!/usr/bin/env python3
from gendiff.formatters.stylish import standard_formatter
from gendiff.formatters.plain import plain_formatter
from gendiff.formatters.json import json_formatter
from gendiff.file_opener import format_opening


def diff_tree(file1, file2):
    result = []
    keys1, keys2 = file1.keys(), file2.keys()
    all_keys = keys1 | keys2
    for key in sorted(all_keys):
        if key not in keys1:
            step_result = {
                'name': key,
                'status': 'added',
                'what_added': file2.get(key)
            }
            result.append(step_result)
        elif key not in keys2:
            step_result = {
                'name': key,
                'status': 'deleted',
                'what_deleted': file1.get(key)
            }
            result.append(step_result)
        elif file1.get(key) == file2.get(key):
            step_result = {
                'name': key,
                'status': 'unchanged',
                'intact': file1.get(key)
            }
            result.append(step_result)
        elif isinstance(
            file1.get(key), dict) and isinstance(
                file2.get(key), dict):
            step_result = {
                'name': key,
                'status': 'nested',
                'children': diff_tree(
                    file1.get(key), file2.get(key))
            }
            result.append(step_result)
        else:
            step_result = {
                'name': key,
                'status': 'changed',
                'from_first_dict': file1.get(key),
                'from_second_dict': file2.get(key)
            }
            result.append(step_result)
    diff = sorted(result, key=lambda x: x['name'])
    return diff


def generate_diff(path1, path2, format='stylish'):
    file1 = format_opening(path1)
    file2 = format_opening(path2)
    diff = diff_tree(file1, file2)
    if format == 'stylish':
        return standard_formatter(diff)
    elif format == 'plain':
        return plain_formatter(diff)
    elif format == 'json':
        return json_formatter(diff)
    else:
        return 'Unknown formatter!'
