def to_str(item):
    if item is None:
        return 'null'
    elif type(item) is bool:
        return str(item).lower()
    elif type(item) is str:
        return f"'{str(item)}'"
    elif type(item) is dict:
        return '[complex value]'
    else:
        return str(item)


def plain_formatter(diff, cur_name=''):
    output = ''
    for diff_unit in diff:
        status = diff_unit['status']
        name = cur_name + diff_unit['name']
        match status:
            case 'added':
                output += f"Property '{name}' "
                output += "was added with value: "
                output += f"{to_str(diff_unit['what_added'])}\n"
            case 'deleted':
                output += f"Property '{name}' was removed\n"
            case 'changed':
                output += f"Property '{name}' was updated. "
                output += f"From {to_str(diff_unit['from_first_dict'])} to "
                output += f"{to_str(diff_unit['from_second_dict'])}\n"
            case 'nested':
                output += plain_formatter(diff_unit['children'],
                                          name + '.')
    return output
