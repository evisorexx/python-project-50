from gendiff.formatters.stylish import standard_formatter
from gendiff.formatters.plain import plain_formatter
from gendiff.formatters.json import json_formatter


def formatting_diff(diff, format):
    if format == 'stylish':
        return standard_formatter(diff)
    elif format == 'plain':
        return plain_formatter(diff).rstrip()
    elif format == 'json':
        return json_formatter(diff)
    else:
        return 'Unknown formatter!'
