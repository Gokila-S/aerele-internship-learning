def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        pass


content = read_file("data.txt")
print(content)
