def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age % 2 == 0:
        print(f"Your age ({age}) is even.")
    else:
        print(f"Your age ({age}) is odd.")

def main():
    try:
        user_input = input("Enter your age: ")
        age = int(user_input)
        check_age(age)
    except ValueError as e:
        print("Error:", e)

main()