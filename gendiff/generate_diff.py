#!/usr/bin/env python3
import json


def tf_to_json(item):
    if item is True:
        return 'true'
    if item is False:
        return 'false'
    return item


def generate_diff(path1, path2):
    file1 = json.load(open(path1, 'r'))
    file2 = json.load(open(path2, 'r'))

    items1 = sorted(file1.items())
    items2 = sorted(file2.items())
    output = '{\n'

    for item in items1:
        if file2.get(item[0]) is not None:
            if file1[item[0]] == file2[item[0]]:
                output += f'    {item[0]}: {tf_to_json(item[1])}\n'
            else:
                output += f'  - {item[0]}: {tf_to_json(item[1])}\n'
                output += f'  + {item[0]}: {tf_to_json(file2[item[0]])}\n'
        else:
            output += f'  - {item[0]}: {tf_to_json(item[1])}\n'

    for item in items2:
        if file1.get(item[0]) is None:
            output += f'  + {item[0]}: {tf_to_json(item[1])}\n'

    return output + '}'
