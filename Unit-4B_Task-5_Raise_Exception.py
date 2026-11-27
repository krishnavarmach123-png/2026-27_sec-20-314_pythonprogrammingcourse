try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Not eligible! Age must be 18+")
    print("Eligible, Age:", age)

except ValueError as e:
    print("Error:", e)