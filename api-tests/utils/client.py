# api-tests/utils/client.py
import os
import requests

# You can change this later to your real backend URL
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

def post_login(payload: dict):
    """Send a login request to the API."""
    return requests.post(f"{BASE_URL}/login", json=payload)

def post_register(payload: dict):
    """Send a registration request to the API."""
    return requests.post(f"{BASE_URL}/register", json=payload)
