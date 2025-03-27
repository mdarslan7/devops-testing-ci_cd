import pytest
import requests

testcases = [
    ("http://127.0.0.1:8000/add/10/5", 15, "Addition"),
    ("http://127.0.0.1:8000/add/-3/3", 0, "Addition of negative"),
]

@pytest.mark.parametrize("url, expected, description", testcases)
def test_api(url, expected, description):
    response = requests.get(url)
    result = response.json()["result"]
    assert result == expected, f"{description} FAILED! Expected {expected}, got {result}"