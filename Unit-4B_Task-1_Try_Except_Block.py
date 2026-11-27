try:
    a = int(input("Enter a number: "))
    print("Square:", a * a)

except ValueError:
    print("Error: Enter only number!")