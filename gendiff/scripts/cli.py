#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff
from gendiff.opener import format_opening
from gendiff.formatters.stylish import standard_formatter
from gendiff.formatters.plain import plain_formatter


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help='set format of output', default='stylish')
    args = parser.parse_args()
    data1 = format_opening(args.first_file)
    data2 = format_opening(args.second_file)
    if args.format == 'plain':
        print(plain_formatter(generate_diff(data1, data2)))
    elif args.format == 'stylish':
        print(standard_formatter(generate_diff(data1, data2)))
    else:
        print('Unknown formatter!')


if __name__ == '__main__':
    main()
