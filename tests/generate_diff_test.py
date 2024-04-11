from gendiff.generate_diff import generate_diff
from gendiff.file_opener import file_opening
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

RESULTS = [
    'This is list of correct results for generate_diff function.',
    './tests/fixtures/results/default_result.txt',       # 1
    './tests/fixtures/results/nested_result.txt',        # 2
    './tests/fixtures/results/for_plain_formatter.txt',  # 3
    './tests/fixtures/results/for_json_formatter.txt',   # 4
    './tests/fixtures/results/empty_json.txt',           # 5
    './tests/fixtures/results/empty_yaml.txt',           # 6
    './tests/fixtures/results/identical.txt',            # 7
]


@pytest.mark.parametrize('name1, name2, formatter, exp_res', [
    (PLAIN_TESTS[1], PLAIN_TESTS[2], 'stylish', RESULTS[1]),    # DEF JSON
    (PLAIN_TESTS[3], PLAIN_TESTS[4], 'stylish', RESULTS[1]),    # DEF YAML
    (NESTED_TESTS[1], NESTED_TESTS[2], 'stylish', RESULTS[2]),  # NEST JSON
    (NESTED_TESTS[3], NESTED_TESTS[4], 'stylish', RESULTS[2]),  # NEST YAML
    (NESTED_TESTS[1], NESTED_TESTS[2], 'plain', RESULTS[3]),    # PLAIN JSON
    (NESTED_TESTS[3], NESTED_TESTS[4], 'plain', RESULTS[3]),    # PLAIN YAML
    (NESTED_TESTS[1], NESTED_TESTS[2], 'json', RESULTS[4]),     # JSON JSON
    (NESTED_TESTS[3], NESTED_TESTS[4], 'json', RESULTS[4]),     # JSON YAML
    (PLAIN_TESTS[1], PLAIN_TESTS[5], 'stylish', RESULTS[5]),    # EMPTY JSON
    (PLAIN_TESTS[6], PLAIN_TESTS[2], 'stylish', RESULTS[6]),    # EMPTY YAML
    (PLAIN_TESTS[1], PLAIN_TESTS[1], 'stylish', RESULTS[7]),    # IDENTICAL JSON
    (PLAIN_TESTS[1], PLAIN_TESTS[1], 'stylish', RESULTS[7])     # IDENTICAL YAML
])
def test_generate_diff(name1, name2, formatter, exp_res):
    result = generate_diff(name1, name2, formatter)
    expected = open(exp_res, 'r').read()
    assert result == expected


def test_unexisting_format():
    result = generate_diff(PLAIN_TESTS[1],
                           PLAIN_TESTS[1], 'nonsense')
    assert result == 'Unknown formatter!'


def test_unexisting_file():
    with pytest.raises(SystemExit) as ex:
        file_opening('./err.txt')
    assert ex.type == SystemExit
