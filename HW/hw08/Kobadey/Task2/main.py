from validator import validate_password

password = input("Enter password: ")
flag = validate_password(password)

while not flag:
    password = input("Try again: ")
    flag = validate_password(password)
