try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Result:", a / b)

except ValueError:
    print("Error: Enter only numbers!")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except Exception as e:
    print("Error:", e)