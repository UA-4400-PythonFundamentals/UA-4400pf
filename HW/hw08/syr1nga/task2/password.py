import re

def check(password):
    if len(password) < 6 or len(password) > 16:
        return False, "Пароль має бути від 6 до 16 символів"
    if not re.search(r"[a-z]", password):
        return False, "Пароль має містити хоча б одну маленьку літеру"
    if not re.search(r"[A-Z]", password):
        return False, "Пароль має містити хоча б одну велику літеру"
    if not re.search(r"\d", password):
        return False, "Пароль має містити хоча б одну цифру"
    if not re.search(r"[$#@]", password):
        return False, "Пароль має містити хоча б один спецсимвол: $, # або @"
    if not re.fullmatch(r"[A-Za-z\d$#@]+", password):
        return False, "Пароль містить недопустимі символи"
    return True, "Пароль валідний"

password = input("Введіть пароль: ")
valid, message = check(password)
print(message)
