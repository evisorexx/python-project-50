from gendiff.generate_diff import generate_diff
from gendiff.opener import format_opening
from gendiff.stylish import formatter
import pytest

PLAIN_TESTS = [
    'This is list of plain test dicts.',
    format_opening('./tests/fixtures/test1.json'), #1 JSON
    format_opening('./tests/fixtures/test2.json'), #2 JSON
    format_opening('./tests/fixtures/test1.yml'),  #3 YAML
    format_opening('./tests/fixtures/test2.yml'),  #4 YAML
    format_opening('./tests/fixtures/empty.json'), #5 JSON EMPTY
    format_opening('./tests/fixtures/empty.yml'),  #6 YAML EMPTY
]

NESTED_TESTS = [
    'This is list of nested test dicts.',
    format_opening('./tests/fixtures/nested1.json'), #1 JSON
    format_opening('./tests/fixtures/nested2.json'), #2 JSON
    format_opening('./tests/fixtures/nested1.yml'),  #3 YAML
    format_opening('./tests/fixtures/nested2.yml'),  #4 YAML
]


def test_diff_json():
    result = formatter(
        generate_diff(PLAIN_TESTS[1], PLAIN_TESTS[2]))
    assert result == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_diff_yml():
    result = formatter(
        generate_diff(PLAIN_TESTS[3], PLAIN_TESTS[4]))
    assert result == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_diff_nested_json():
    result = formatter(
        generate_diff(NESTED_TESTS[1], NESTED_TESTS[2]))
    assert result == '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


def test_diff_nested_yml():
    result = formatter(
        generate_diff(NESTED_TESTS[3], NESTED_TESTS[4]))
    assert result == '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


def test_with_empty_file():
    result_json = formatter(
        generate_diff(PLAIN_TESTS[1], PLAIN_TESTS[5]))
    result_yml = formatter(
        generate_diff(PLAIN_TESTS[6], PLAIN_TESTS[2]))
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
    result_json = formatter(
        generate_diff(PLAIN_TESTS[1], PLAIN_TESTS[1]))
    result_yml = formatter(
        generate_diff(PLAIN_TESTS[3], PLAIN_TESTS[3]))
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


def test_format():
    with pytest.raises(SystemExit) as ex:
        format_opening('./err.txt')
    assert ex.type == SystemExit

print(PLAIN_TESTS[1])