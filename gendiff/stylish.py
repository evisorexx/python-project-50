#!/usr/bin/env python3
ADD, DEL, DEF = '  + ', '  - ', '    '


def values_format(item, depth):
    if len(str(item)) == 0:
        return ''
    if type(item) is bool:
        return str(item).lower()
    elif type(item) is dict:
        represent = '{\n'
        for elem in item.items():
            if type(elem[1]) is dict:
                represent += f'{DEF * (depth + 1)}{elem[0]}: '
                represent += values_format(elem[1], depth + 1)
                represent += '\n'
            else:
                represent += f'{DEF * (depth + 1)}{elem[0]}: {elem[1]}\n'
        represent += f'{DEF * depth}}}'
        return represent
    else:
        return item


def formatter(diff):
    output = '{\n'
    def making_indents(current_diff, depth=1):
        nonlocal output
        for diff_unit in current_diff:
            status = diff_unit['status']
            match status:
                case 'added':
                    output += f'{DEF * (depth - 1) + ADD}{diff_unit["name"]}: '
                    output += f'{values_format(diff_unit["what_added"], depth)}\n'
                case 'deleted':
                    output += f'{DEF * (depth - 1) + DEL}{diff_unit["name"]}: '
                    output += f'{values_format(diff_unit["what_deleted"], depth)}\n'
                case 'unchanged':
                    output += f'{DEF * depth}{diff_unit["name"]}: '
                    output += f'{values_format(diff_unit["intact"], depth)}\n'
                case 'changed':
                    output += f'{DEF * (depth - 1) + DEL}{diff_unit["name"]}: '
                    output += f'{values_format(diff_unit["from_first_dict"], depth)}\n'
                    output += f'{DEF * (depth - 1) + ADD}{diff_unit["name"]}: '
                    output += f'{values_format(diff_unit["from_second_dict"], depth)}\n'
                case 'nested':
                    output += f'{DEF * depth}{diff_unit["name"]}: {{\n'
                    making_indents(diff_unit['children'], depth + 1)
                    output += DEF * depth + '}\n'
    making_indents(diff)
    return output + '}'
