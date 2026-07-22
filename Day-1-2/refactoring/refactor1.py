def double_even_numbers(numbers: list[int]) -> list[int]:
    """Return a list containing double the value of each even number."""

    return [number * 2 for number in numbers if number % 2 == 0]