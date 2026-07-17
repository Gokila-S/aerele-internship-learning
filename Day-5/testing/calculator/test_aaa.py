from calculator import add


def test_add():
    # Arrange
    a = 2
    b = 3

    # Act
    result = add(a, b)

    # Assert
    assert result == 5
