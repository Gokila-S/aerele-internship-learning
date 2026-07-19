numbers = [1, 2, 3, 4, 5]
squares = []

for i in range(len(numbers)):
    squares.append(numbers[i] * numbers[i])

print("Java-style:", squares)


pythonic_squares = [n * n for n in numbers]
print("Pythonic:", pythonic_squares)


# Context Manager
with open("output.txt", "w") as file:
    file.write(str(pythonic_squares))

print("Data written to output.txt")