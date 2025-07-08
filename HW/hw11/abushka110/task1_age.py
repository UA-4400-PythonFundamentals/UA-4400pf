def check_age_oe(age: int):
    if age < 0:
        raise ValueError("negative")
    if age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."

def main():
    try:
        user_input = input("Enter your age: ")
        age = int(user_input)  # може згенерувати ValueError (якщо введено текст)
        result = check_age_oe(age)  # може згенерувати ValueError (якщо age < 0)
        print(result)

    except ValueError as ve:
        if str(ve) == "negative":
            print("Age cannot be negative.")
        else:
            print("Your age can only be a number.")

if __name__ == "__main__":
    main()