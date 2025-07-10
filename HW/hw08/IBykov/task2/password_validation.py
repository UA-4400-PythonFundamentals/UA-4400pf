def check_password(password):
    if len(password) < 6:
        return False, "Пароль занадто короткий! Мінімум 6 символів."

    if len(password) > 16:
        return False, "Пароль занадто довгий! Максимум 16 символів."

    has_lowercase = False
    for char in password:
        if char >= 'a' and char <= 'z':
            has_lowercase = True
            break

    if not has_lowercase:
        return False, "Пароль повинен містити хоча б одну маленьку літеру [a-z]."

    has_uppercase = False
    for char in password:
        if char >= 'A' and char <= 'Z':
            has_uppercase = True
            break

    if not has_uppercase:
        return False, "Пароль повинен містити хоча б одну велику літеру [A-Z]."

    has_digit = False
    for char in password:
        if char >= '0' and char <= '9':
            has_digit = True
            break

    if not has_digit:
        return False, "Пароль повинен містити хоча б одну цифру [0-9]."

    special_chars = "$#@"
    has_special = False
    for char in password:
        if char in special_chars:
            has_special = True
            break

    if not has_special:
        return False, "Пароль повинен містити хоча б один спеціальний символ [$#@]."

    return True, "Пароль валідний!"


def main():
    print("Перевірка пароля")
    print("Вимоги до пароля:")
    print("- Мінімум 6 символів, максимум 16")
    print("- Хоча б одна маленька літера [a-z]")
    print("- Хоча б одна велика літера [A-Z]")
    print("- Хоча б одна цифра [0-9]")
    print("- Хоча б один спеціальний символ [$#@]")
    print()

    while True:
        password = input("Введіть пароль для перевірки: ")

        is_valid, message = check_password(password)

        if is_valid:
            print(message)
        else:
            print(message)

        print()


if __name__ == "__main__":
    main()