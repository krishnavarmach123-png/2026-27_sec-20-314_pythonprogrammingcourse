while True:
    try:
        age = int(input("Enter your age: "))
        if 1 <= age <= 120:
            break
        print("Age must be 1 to 120")
    except ValueError:
        print("Invalid! Enter only number")

print("Your Age:", age)