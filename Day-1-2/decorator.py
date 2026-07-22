def greet_decorator(func):
    def wrapper():
        print("Before Greeting")
        func()
        print("After Greeting")
    return wrapper


@greet_decorator
def greet():
    print("Hello!")


greet()