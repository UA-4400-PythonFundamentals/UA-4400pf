def check_age_even_odd(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age % 2 == 0:
        return "The age is even."
    else:
        return "The age is odd."

def main():
    try:
        user_input = input("Enter your age: ")
        age = int(user_input)
        result = check_age_even_odd(age)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()