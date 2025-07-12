def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print(f"Error: {e}")
except:
    print("Error: Please enter a valid number")