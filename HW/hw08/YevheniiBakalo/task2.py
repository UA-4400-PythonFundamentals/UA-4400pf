import re

def is_valid(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[$#@]', password):
        return False
    return True

def main():
    password = input("Input your password: ")
    if is_valid(password):
        print("Valid password")
    else:
        print("Invalid password")

if __name__ == "__main__":
    main()
