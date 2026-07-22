def div(a, b):
    return a / b


try:
    div(10, 0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
