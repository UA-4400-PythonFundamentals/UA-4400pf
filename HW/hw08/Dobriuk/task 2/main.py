print(">>> main.py загружен, __name__ =", __name__)

from validators import validate_password

if __name__ == "__main__":
    while True:
        password = input("Enter your password: ")
        errors = validate_password(password)
        if not errors:
            print("Your password is valid.")
            break
        print("Your password is invalid.")
        for error in errors:
            print("  -", error)
        print("try again.")