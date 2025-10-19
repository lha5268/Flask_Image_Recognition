"""
Redefines the client for the scope of the application.
"""

import pytest
from app import app  # This imports the Flask app for testing

@pytest.fixture
def client():
    """
    Redefine client for the scope of the app.
    """
    with app.test_client() as client:
        yield client
