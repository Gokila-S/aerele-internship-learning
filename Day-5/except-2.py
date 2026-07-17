def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


try:
    div(10, 0)
except Exception as e:
    print(f"Error: {e}")
