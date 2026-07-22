def calculate_average(marks: list[int]) -> float:
    """Calculate the average marks."""
    if not marks:
        raise ValueError("Marks list cannot be empty")

    return sum(marks) / len(marks)


def get_result(average: float) -> str:
    """Return Pass or Fail."""
    return "Pass" if average >= 50 else "Fail"


def process_marks(marks: list[int]) -> str:
    """Process student marks."""
    average = calculate_average(marks)
    return get_result(average)


print(process_marks([70, 60, 80]))
print(process_marks([20, 30, 40]))