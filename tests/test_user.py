import pytest
import requests
import requests_mock

def test_users_endpoint(requests_mock):
    # Define the URL and parameters
    url = "http://127.0.0.1:8000/users/"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Mock the GET request
    requests_mock.get(url, text='', status_code=200)

    # Make the GET request
    response = requests.get(url, params=params)

    # Verify the response status code
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Verify the response body is empty
    assert response.text == "", f"Expected empty response, got: {response.text}"

def test_users_endpoint_unauthorized(requests_mock):
    # Define the URL and parameters
    url = "http://127.0.0.1:8000/users/"
    params = {
        "username": "admin",
        "password": "admin"
    }

    # Mock the GET request
    requests_mock.get(url, text='', status_code=401)

    # Make the GET request
    response = requests.get(url, params=params)

    # Verify the response status code
    assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"

    # Verify the response body is empty
    assert response.text == "", f"Expected empty response, got: {response.text}"

if __name__ == '__main__':
    pytest.main([__file__])
