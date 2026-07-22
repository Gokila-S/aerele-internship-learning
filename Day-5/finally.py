try:
    file = open("data.txt")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing resources.")
