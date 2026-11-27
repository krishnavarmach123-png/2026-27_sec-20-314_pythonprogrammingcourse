try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = a / b
except ValueError:
    print("Enter only numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result:", result)
finally:
    print("Program Finished")