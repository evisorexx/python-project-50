#!/usr/bin/env python3
def to_str(item):
    if item is None:
        return 'null'
    elif type(item) is bool:
        return str(item).lower()
    elif type(item) is str:
        return f"'{str(item)}'"
    else:
        return str(item)


def plain_formatter(diff, cur_name=''):
    output = ''
    for diff_unit in diff:
        status = diff_unit['status']
        name = cur_name + diff_unit['name']
        match status:
            case 'added':
                if isinstance(diff_unit['what_added'], dict):
                    output += f"Property '{name}' was "
                    output += "added with value: [complex value]\n"
                else:
                    output += f"Property '{name}' "
                    output += "was added with value: "
                    output += f"{to_str(diff_unit['what_added'])}\n"
            case 'deleted':
                output += f"Property '{name}' was removed\n"
            case 'changed':
                output += f"Property '{name}' was updated. "
                if isinstance(diff_unit['from_first_dict'], dict):
                    output += "From [complex value] to "
                    output += f"{to_str(diff_unit['from_second_dict'])}\n"
                elif isinstance(diff_unit['from_second_dict'], dict):
                    output += f"From {to_str(diff_unit['from_first_dict'])} "
                    output += "to [complex value]\n"
                else:
                    output += f"From {to_str(diff_unit['from_first_dict'])} "
                    output += f"to {to_str(diff_unit['from_second_dict'])}\n"
            case 'nested':
                output += plain_formatter(diff_unit['children'],
                                          name + '.')
    return output
