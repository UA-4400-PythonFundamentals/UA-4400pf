def main():
    age = int(input("What is your age? "))
    process_age(age)


def process_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    if age % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

main()
