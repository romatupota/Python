users = {
    "user_1": {
        "first_name": input("Enter your name: "),
        "last_name": input("Enter your last name: "),
        "age": int(input("enter your age: "))
    }
}
print("Are you?")
print(users["user_1"].values())