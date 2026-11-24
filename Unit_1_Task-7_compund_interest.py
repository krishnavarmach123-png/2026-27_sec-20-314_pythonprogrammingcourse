principle = float(input("Enter Principle Amount(in rupees): "))
rate = float(input("Enter Annual Interest Rate (in percentage): "))
time = float(input("Enter the time (in years) : "))
amount = principle * (1 + (rate / 100) **(time))
compound  = amount - principle
print("COMPOUND INTEREST",compound )