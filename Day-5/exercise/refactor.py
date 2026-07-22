def calculate_average(numbers : list[int]) -> float:
    """Used to calculate average for a list of numbers"""
    if not numbers:
        raise ValueError("List cannot be empty")
    total = 0
    for n in numbers:
        total += n

    average = total/len(numbers)
    return average

def result(numbers:list[int])->str:
    """used to find if a student is pass or fail"""
    try:
        avg = calculate_average(numbers)
        if avg > 50 :
            return "pass"
        return "fail"
    except ValueError as e:
        print(e)

print(result([10,10,20]))
print(result([70,50,50]))
print(result([]))