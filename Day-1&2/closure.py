from collections.abc import Callable


def make_multiplier(factor: int) -> Callable[[int], int]:
    def multiply(number: int) -> int:
        return number * factor

    return multiply


def run_demo() -> None:
    double = make_multiplier(2)
    print(double(5))


if __name__ == "__main__":
    run_demo()
def make_multiplier(factor: int) -> Callable[[int], int]:
    def multiply(number: int) -> int:
        return number * factor
    return multiply

double = make_multiplier(2)
print(double(5))  # Output: 10