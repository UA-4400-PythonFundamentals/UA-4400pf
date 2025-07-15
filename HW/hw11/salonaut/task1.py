def check_age(age: int):
    if age <= 0:
        raise ValueError('Age can\'t be negative')

    return 'Even' if age % 2 == 0 else 'Odd'



if __name__ == "__main__":
    try:
        age = int(input('Enter your age:'))
        res = check_age(age)
        print(res)
    except ValueError as e:
        print(e)