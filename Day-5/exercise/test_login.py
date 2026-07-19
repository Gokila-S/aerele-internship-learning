import pytest
from new_login import User, login


def test_valid_login():
    user = User("Goki", "admin123")
    assert login(user) == "Login Successful"


def test_invalid_login():
    user = User("Goki", "12345")
    assert login(user) == "Login Failed"


def test_empty_username():
    with pytest.raises(ValueError, match="Username cannot be empty"):
        login(User("", "admin123"))