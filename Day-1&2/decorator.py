from collections.abc import Callable


def log_execution(func: Callable[..., int]) -> Callable[..., int]:
    def wrapper(*args, **kwargs):
        print(f"running {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished {func.__name__}")
        return result

    return wrapper


@log_execution
def calculate_sum(a: int, b: int) -> int:
    return a + b


def run_demo() -> None:
    print(calculate_sum(10, 20))


if __name__ == "__main__":
    run_demo()
def log_execution(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"🚀 Executing: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished: {func.__name__}")
        return result
    return wrapper

@log_execution
def calculate_sum(a: int, b: int) -> int:
    return a + b

print(calculate_sum(10, 20))