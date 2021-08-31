import pytest
import requests

def test_get_employee():
    response = requests.get("https://dummy.restapiexample.com/api/v1/employees")
    print(response.status_code)
    print(response.text)
    assert response.ok