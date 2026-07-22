def multiply(a, b):
    return a + b


# asset is a keyword in python to verify the o/p of a function with expected o/p
# if the o/p is not as expected, it will throw an error. Else nothing happens.
assert multiply(2, 3) == 6
assert multiply(10, 20) == 200
