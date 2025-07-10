import string


def check_password(pwd):
    if len(pwd) < 6:
        return False

    if len(pwd) > 16:
        return False

    if not any(char in string.ascii_lowercase for char in pwd):
        return False

    if not any(char in string.ascii_uppercase for char in pwd):
        return False

    if not any(char in ['$', '#', '@'] for char in pwd):
        return False

    if not any(char.isdigit() for char in pwd):
        return False
    
    return True

password = input("Введіть пароль: ")

if check_password(password):
    print("Пароль підходить")
else:
    print("Пароль не підходить")
