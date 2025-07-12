def check_age(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative.")
    except ValueError as e:
        return e
    else:
        if age % 2 == 0:
            return "You are an even-aged person."
        else:
            return "You are an odd-aged person."
        
user_input = input("Enter your age: ")
result = check_age(user_input)
print(result)