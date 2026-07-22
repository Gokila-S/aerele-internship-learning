import math

def calculate(numbers):
    total = 0

    for i in range(len(numbers)):
        total = total + numbers[i]

    average = total / len(numbers)

    print("Average:", average)

    if average > 50:
        return True
    else:
        return False

print(calculate([10,10,20]))
print(calculate([70,50,50]))
print(calculate([]))