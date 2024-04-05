from gendiff.generate_diff import generate_diff
from gendiff.file_opener import format_opening
import pytest

PLAIN_TESTS = [
    'This is list of plain test dicts.',
    './tests/fixtures/default1.json', #1 JSON
    './tests/fixtures/default2.json', #2 JSON
    './tests/fixtures/default1.yml',  #3 YAML
    './tests/fixtures/default2.yml',  #4 YAML
    './tests/fixtures/empty.json', #5 JSON EMPTY
    './tests/fixtures/empty.yml',  #6 YAML EMPTY
]

NESTED_TESTS = [
    'This is list of nested test dicts.',
    './tests/fixtures/nested1.json', #1 JSON
    './tests/fixtures/nested2.json', #2 JSON
    './tests/fixtures/nested1.yml',  #3 YAML
    './tests/fixtures/nested2.yml',  #4 YAML
]


def test_diff_json():
    result = generate_diff(PLAIN_TESTS[1],
                            PLAIN_TESTS[2], 'stylish')
    assert result == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_diff_yml():
    result = generate_diff(PLAIN_TESTS[3],
                            PLAIN_TESTS[4], 'stylish')
    assert result == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_diff_nested_json():
    result = generate_diff(NESTED_TESTS[1],
                            NESTED_TESTS[2], 'stylish')
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
    result = generate_diff(NESTED_TESTS[3],
                            NESTED_TESTS[4], 'stylish')
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


def test_plain_frmt_yml():
    result_def = generate_diff(PLAIN_TESTS[3],
                               PLAIN_TESTS[4], 'plain')
    result_nested = generate_diff(NESTED_TESTS[3],
                                   NESTED_TESTS[4], 'plain')
    assert result_nested == '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
'''
    assert result_def == '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
'''


def test_plain_frmt_json():
    result_def = generate_diff(PLAIN_TESTS[1],
                                PLAIN_TESTS[2], 'plain')
    result_nested = generate_diff(NESTED_TESTS[1],
                                   NESTED_TESTS[2], 'plain')
    assert result_nested == '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
'''
    assert result_def == '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
'''


def test_json_frmt_json():
    result_def = generate_diff(PLAIN_TESTS[1],
                                PLAIN_TESTS[2], 'json')
    result_nested = generate_diff(NESTED_TESTS[1],
                                   NESTED_TESTS[2], 'json')
    assert result_def == '''[
    {
        "name": "follow",
        "status": "deleted",
        "what_deleted": false
    },
    {
        "name": "host",
        "status": "unchanged",
        "intact": "hexlet.io"
    },
    {
        "name": "proxy",
        "status": "deleted",
        "what_deleted": "123.234.53.22"
    },
    {
        "name": "timeout",
        "status": "changed",
        "from_first_dict": 50,
        "from_second_dict": 20
    },
    {
        "name": "verbose",
        "status": "added",
        "what_added": true
    }
]'''
    assert result_nested == '''[
    {
        "name": "common",
        "status": "nested",
        "children": [
            {
                "name": "follow",
                "status": "added",
                "what_added": false
            },
            {
                "name": "setting1",
                "status": "unchanged",
                "intact": "Value 1"
            },
            {
                "name": "setting2",
                "status": "deleted",
                "what_deleted": 200
            },
            {
                "name": "setting3",
                "status": "changed",
                "from_first_dict": true,
                "from_second_dict": null
            },
            {
                "name": "setting4",
                "status": "added",
                "what_added": "blah blah"
            },
            {
                "name": "setting5",
                "status": "added",
                "what_added": {
                    "key5": "value5"
                }
            },
            {
                "name": "setting6",
                "status": "nested",
                "children": [
                    {
                        "name": "doge",
                        "status": "nested",
                        "children": [
                            {
                                "name": "wow",
                                "status": "changed",
                                "from_first_dict": "",
                                "from_second_dict": "so much"
                            }
                        ]
                    },
                    {
                        "name": "key",
                        "status": "unchanged",
                        "intact": "value"
                    },
                    {
                        "name": "ops",
                        "status": "added",
                        "what_added": "vops"
                    }
                ]
            }
        ]
    },
    {
        "name": "group1",
        "status": "nested",
        "children": [
            {
                "name": "baz",
                "status": "changed",
                "from_first_dict": "bas",
                "from_second_dict": "bars"
            },
            {
                "name": "foo",
                "status": "unchanged",
                "intact": "bar"
            },
            {
                "name": "nest",
                "status": "changed",
                "from_first_dict": {
                    "key": "value"
                },
                "from_second_dict": "str"
            }
        ]
    },
    {
        "name": "group2",
        "status": "deleted",
        "what_deleted": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    {
        "name": "group3",
        "status": "added",
        "what_added": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
]'''


def test_json_frmt_yml():
    result_def = generate_diff(PLAIN_TESTS[3],
                                PLAIN_TESTS[4], 'json')
    result_nested = generate_diff(NESTED_TESTS[3],
                                   NESTED_TESTS[4], 'json')
    assert result_def == '''[
    {
        "name": "follow",
        "status": "deleted",
        "what_deleted": false
    },
    {
        "name": "host",
        "status": "unchanged",
        "intact": "hexlet.io"
    },
    {
        "name": "proxy",
        "status": "deleted",
        "what_deleted": "123.234.53.22"
    },
    {
        "name": "timeout",
        "status": "changed",
        "from_first_dict": 50,
        "from_second_dict": 20
    },
    {
        "name": "verbose",
        "status": "added",
        "what_added": true
    }
]'''
    assert result_nested == '''[
    {
        "name": "common",
        "status": "nested",
        "children": [
            {
                "name": "follow",
                "status": "added",
                "what_added": false
            },
            {
                "name": "setting1",
                "status": "unchanged",
                "intact": "Value 1"
            },
            {
                "name": "setting2",
                "status": "deleted",
                "what_deleted": 200
            },
            {
                "name": "setting3",
                "status": "changed",
                "from_first_dict": true,
                "from_second_dict": null
            },
            {
                "name": "setting4",
                "status": "added",
                "what_added": "blah blah"
            },
            {
                "name": "setting5",
                "status": "added",
                "what_added": {
                    "key5": "value5"
                }
            },
            {
                "name": "setting6",
                "status": "nested",
                "children": [
                    {
                        "name": "doge",
                        "status": "nested",
                        "children": [
                            {
                                "name": "wow",
                                "status": "changed",
                                "from_first_dict": "",
                                "from_second_dict": "so much"
                            }
                        ]
                    },
                    {
                        "name": "key",
                        "status": "unchanged",
                        "intact": "value"
                    },
                    {
                        "name": "ops",
                        "status": "added",
                        "what_added": "vops"
                    }
                ]
            }
        ]
    },
    {
        "name": "group1",
        "status": "nested",
        "children": [
            {
                "name": "baz",
                "status": "changed",
                "from_first_dict": "bas",
                "from_second_dict": "bars"
            },
            {
                "name": "foo",
                "status": "unchanged",
                "intact": "bar"
            },
            {
                "name": "nest",
                "status": "changed",
                "from_first_dict": {
                    "key": "value"
                },
                "from_second_dict": "str"
            }
        ]
    },
    {
        "name": "group2",
        "status": "deleted",
        "what_deleted": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    {
        "name": "group3",
        "status": "added",
        "what_added": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
]'''


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


def test_format():
    with pytest.raises(SystemExit) as ex:
        format_opening('./err.txt')
    assert ex.type == SystemExit
