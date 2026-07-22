def uppercase(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper


@uppercase
def greet(name):
    return f"Hello {name}"


print(greet("Goki"))