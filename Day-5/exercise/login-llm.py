def login(user):
    if user["password"] == "admin123":
        print("Login Successful")
        return True

    print("Login Failed")


print(login({"username": "Goki", "password": "admin123"}))
print(login({"username": "Goki", "password": "12345"}))
print(login({"username": "Goki"}))  