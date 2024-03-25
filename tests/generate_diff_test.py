from gendiff.generate_diff import generate_diff
import pytest


def test_diff_json():
    result = generate_diff('./tests/fixtures/test1.json',
                           './tests/fixtures/test2.json')
    assert result == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_diff_yml():
    result = generate_diff('./tests/fixtures/test1.yml',
                           './tests/fixtures/test2.yml')
    assert result == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_diff_nested_json():
    result = generate_diff('./tests/fixtures/nested1.json',
                           './tests/fixtures/nested2.json')
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
}
'''


def test_diff_nested_yml():
    result = generate_diff('./tests/fixtures/nested1.yml',
                           './tests/fixtures/nested2.yml')
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
}
'''


def test_with_empty_file():
    result_json = generate_diff('./tests/fixtures/test1.json',
                           './tests/fixtures/empty.json')
    result_yml = generate_diff('./tests/fixtures/empty.yml',
                           './tests/fixtures/test2.yml')
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
    result_json = generate_diff('./tests/fixtures/test1.json',
                           './tests/fixtures/test1.json')
    result_yml = generate_diff('./tests/fixtures/test1.yml',
                           './tests/fixtures/test1.yml')
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
        generate_diff('./err.txt',
                      './tests/fixtures/test1.json')
    assert ex.type == SystemExit
    
    with pytest.raises(SystemExit) as ex:
        generate_diff('./tests/fixtures/test1.yml',
                      './err.rar')
    assert ex.type == SystemExit
