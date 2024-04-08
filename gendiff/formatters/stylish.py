ADD, DEL, DEF = '  + ', '  - ', '    '


def to_str(key, value, depth):
    if value is None:
        return f'{key}: null'
    elif type(value) is bool:
        return f'{key}: {str(value).lower()}'
    elif type(value) is dict:
        lines = [f'{key}: {{']
        for item in value.items():
            lines.append(
                DEF * (depth + 1) + to_str(
                    item[0], item[1], depth + 1))
        lines.append((DEF * (depth)) + '}')
        return '\n'.join(lines)
    else:
        return f'{key}: {str(value)}'


def standard_formatter(diff):
    def making_indents(current_diff, depth=1):
        lines = []
        for diff_unit in current_diff:
            status = diff_unit['status']
            match status:
                case 'added':
                    lines.append(
                        (DEF * (depth - 1) + ADD) + to_str(
                            diff_unit['name'], diff_unit['what_added'],
                            depth
                        ))
                case 'deleted':
                    lines.append(
                        (DEF * (depth - 1) + DEL) + to_str(
                            diff_unit['name'], diff_unit['what_deleted'],
                            depth
                        ))
                case 'unchanged':
                    lines.append(
                        (DEF * depth) + to_str(
                            diff_unit['name'], diff_unit['intact'],
                            depth
                        ))
                case 'changed':
                    lines.append(
                        (DEF * (depth - 1) + DEL) + to_str(
                            diff_unit['name'], diff_unit['from_first_dict'],
                            depth
                        ))
                    lines.append(
                        (DEF * (depth - 1) + ADD) + to_str(
                            diff_unit['name'], diff_unit['from_second_dict'],
                            depth
                        ))
                case 'nested':
                    nested = making_indents(diff_unit['children'], depth + 1)
                    lines.append(
                        f'{DEF * depth}{diff_unit["name"]}: {nested}')
        output = '{\n' + '\n'.join(lines) + f"\n{(DEF * (depth - 1))}}}"
        return output
    return making_indents(diff)
