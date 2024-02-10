from gendiff.generate_diff import generate_diff
import pytest


@pytest.fixture
def file1():
    return './gendiff/files/file1.json'


@pytest.fixture
def file2():
    return './gendiff/files/file2.json'

def test_diff(file1, file2):
    result = generate_diff(file1, file2)
    assert result == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''