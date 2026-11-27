class InvalidSpeedError(Exception):
    pass

try:
    speed = int(input("Enter speed: "))
    if speed < 0 or speed > 120:
        raise InvalidSpeedError("Invalid Speed! Must be 0 to 120")
    print("Valid Speed:", speed)

except InvalidSpeedError as e:
    print(e)
except ValueError:
    print("Enter only number")