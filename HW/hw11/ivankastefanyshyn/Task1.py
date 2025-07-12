def your_age(age):
    if age < 0:
        raise ValueError("You entered a negative number. Please try again")
    if age % 2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")


def main():
    try:
        your_age(int(input("Please enter your age:")))
    except ValueError as m:
        print("Mistake:", m)


if __name__ == "__main__":
    main()
