from password_validation import validation, password_requirements
from re_validation import valid_password

password_requirements()

if __name__ == "__main__":
    password_requirements()

    while True:
        user_password = input('Enter password: ')
        if valid_password(user_password):
            print('Your password is valid. ')
            break
        else:
            print('Try again. ')