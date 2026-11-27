try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Result:", a / b)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Enter only numbers!")