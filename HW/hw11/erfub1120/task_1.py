try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(e)
else:
    if age % 2 == 0:
        print("You are an even-aged person.")
    else:
        print("You are an odd-aged person.")