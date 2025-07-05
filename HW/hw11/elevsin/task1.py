def process_age(age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Invalid input: age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age % 2 == 0:
        return f"Your age is even."
    else:
        return f"Your age is odd."

def main():
    age_input = input("Enter your age: ")
    try:
        result = process_age(age_input)
    except ValueError as e:
        print("Error:", e)
    else:
        print(result)

main()
