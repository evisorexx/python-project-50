from gendiff.generate_diff import generate_diff
from gendiff.file_opener import format_opening
import pytest

PLAIN_TESTS = [
    'This is list of plain test dicts.',
    './tests/fixtures/default1.json',  # 1 JSON
    './tests/fixtures/default2.json',  # 2 JSON
    './tests/fixtures/default1.yml',   # 3 YAML
    './tests/fixtures/default2.yml',  # 4 YAML
    './tests/fixtures/empty.json',  # 5 JSON EMPTY
    './tests/fixtures/empty.yml',  # 6 YAML EMPTY
]

NESTED_TESTS = [
    'This is list of nested test dicts.',
    './tests/fixtures/nested1.json',  # 1 JSON
    './tests/fixtures/nested2.json',  # 2 JSON
    './tests/fixtures/nested1.yml',  # 3 YAML
    './tests/fixtures/nested2.yml',  # 4 YAML
]


def test_diff_json():
    result = generate_diff(PLAIN_TESTS[1],
                           PLAIN_TESTS[2], 'stylish')
    assert result == open(
        './tests/fixtures/default_result.txt', 'r').read()


def test_diff_yml():
    result = generate_diff(PLAIN_TESTS[3],
                           PLAIN_TESTS[4], 'stylish')
    assert result == open(
        './tests/fixtures/default_result.txt', 'r').read()


def test_diff_nested_json():
    result = generate_diff(NESTED_TESTS[1],
                           NESTED_TESTS[2], 'stylish')
    assert result == open(
        './tests/fixtures/nested_result.txt', 'r').read()


def test_diff_nested_yml():
    result = generate_diff(NESTED_TESTS[3],
                           NESTED_TESTS[4], 'stylish')
    assert result == open(
        './tests/fixtures/nested_result.txt', 'r').read()


def test_plain_frmt_yml():
    result_def = generate_diff(PLAIN_TESTS[3],
                               PLAIN_TESTS[4], 'plain')
    result_nested = generate_diff(NESTED_TESTS[3],
                                  NESTED_TESTS[4], 'plain')
    assert result_nested == open(
        './tests/fixtures/for_plain_formatter_nest.txt', 'r').read()
    assert result_def == open(
        './tests/fixtures/for_plain_formatter_def.txt', 'r').read()


def test_plain_frmt_json():
    result_def = generate_diff(PLAIN_TESTS[1],
                               PLAIN_TESTS[2], 'plain')
    result_nested = generate_diff(NESTED_TESTS[1],
                                  NESTED_TESTS[2], 'plain')
    assert result_nested == open(
        './tests/fixtures/for_plain_formatter_nest.txt', 'r').read()
    assert result_def == open(
        './tests/fixtures/for_plain_formatter_def.txt', 'r').read()


def test_json_frmt_json():
    result_def = generate_diff(PLAIN_TESTS[1],
                               PLAIN_TESTS[2], 'json')
    result_nested = generate_diff(NESTED_TESTS[1],
                                  NESTED_TESTS[2], 'json')
    assert result_def == open(
        './tests/fixtures/for_json_formatter_def.txt', 'r').read()
    assert result_nested == open(
        './tests/fixtures/for_json_formatter_nest.txt', 'r').read()


def test_json_frmt_yml():
    result_def = generate_diff(PLAIN_TESTS[3],
                               PLAIN_TESTS[4], 'json')
    result_nested = generate_diff(NESTED_TESTS[3],
                                  NESTED_TESTS[4], 'json')
    assert result_def == open(
        './tests/fixtures/for_json_formatter_def.txt', 'r').read()
    assert result_nested == open(
        './tests/fixtures/for_json_formatter_nest.txt', 'r').read()


def test_with_empty_file():
    result_json = generate_diff(PLAIN_TESTS[1],
                                PLAIN_TESTS[5], 'stylish')
    result_yml = generate_diff(PLAIN_TESTS[6],
                               PLAIN_TESTS[2], 'stylish')
    assert result_json == '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''

    assert result_yml == '''{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}'''


def test_identical_files():
    result_json = generate_diff(PLAIN_TESTS[1],
                                PLAIN_TESTS[1], 'stylish')
    result_yml = generate_diff(PLAIN_TESTS[3],
                               PLAIN_TESTS[3], 'stylish')
    assert result_json == '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''

    assert result_yml == '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''


def test_unexisting_format():
    result = generate_diff(PLAIN_TESTS[1],
                           PLAIN_TESTS[1], 'nonsense')
    assert result == 'Unknown formatter!'


def test_unexisting_file():
    with pytest.raises(SystemExit) as ex:
        format_opening('./err.txt')
    assert ex.type == SystemExit
