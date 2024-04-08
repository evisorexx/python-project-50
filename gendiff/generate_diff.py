from gendiff.file_opener import file_opening
from gendiff.formatters.formatter_selection import choose_formatter
from gendiff.diff_tree import generate


def generate_diff(path1, path2, format='stylish'):
    file1 = file_opening(path1)
    file2 = file_opening(path2)
    diff = generate(file1, file2)
    return choose_formatter(diff, format)
