from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str


def validate_user(user: User) -> None:
    """validating user input"""
    if not user.username.strip():
        raise ValueError("Username cannot be empty")

    if not user.password.strip():
        raise ValueError("Password cannot be empty")


def login(user: User) -> str:
    """Simulating user login"""
    validate_user(user)

    if user.password == "admin123":
        return "Login Successful"

    return "Login Failed"


try:
    print(login(User("Goki", "admin123")))
    print(login(User("Goki", "12345")))
    print(login(User("", "12345")))
except ValueError as e:
    print("Error:", e)