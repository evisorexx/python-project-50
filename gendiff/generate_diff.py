from gendiff.file_opener import file_opening
from gendiff.formatters.__init__ import formatting_diff
from gendiff.diff_tree import generate_diff_tree


def generate_diff(path1, path2, format='stylish'):
    file1 = file_opening(path1)
    file2 = file_opening(path2)
    diff = generate_diff_tree(file1, file2)
    return formatting_diff(diff, format)
