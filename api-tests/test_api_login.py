# api-tests/tests_api_login.py
from utils.client import post_login

valid_user = {"email": "user@example.com", "password": "Password123!"}


def test_login_success():
    """Login should succeed with valid credentials."""
    response = post_login(valid_user)
    # In a real API, this should be 200
    assert response.status_code == 200


def test_login_invalid_password():
    """Login should fail with wrong password."""
    bad_user = {"email": "user@example.com", "password": "WrongPassword"}
    response = post_login(bad_user)
    # Many APIs use 400 or 401 for invalid login
    assert response.status_code in (400, 401)
