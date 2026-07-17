def add(a, b):
    return a - b


def greet(name):
    if name is None:
        print("No Name")

    if True:
        print("Always True")

    return "Hello"

    print("This line will never execute")


try:
    result = add(10, 0)
except Exception as e:
    print(e)

print(add(5, 3))
