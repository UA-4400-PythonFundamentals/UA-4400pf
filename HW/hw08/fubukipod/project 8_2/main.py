import re

REQUIREMENTS = [
    (lambda s: 6 <= len(s) <= 16,       "Довжина 6–16 символів"),
    (lambda s: re.search(r"[a-z]", s), "Принаймні одна мала літера [a-z]"),
    (lambda s: re.search(r"[A-Z]", s), "Принаймні одна велика літера [A-Z]"),
    (lambda s: re.search(r"\d", s),    "Принаймні одна цифра [0-9]"),
    (lambda s: re.search(r"[$#@]", s), "Принаймні один із символів $, #, @")
]

def validate(pwd: str) -> list:    
    return [msg for check, msg in REQUIREMENTS if not check(pwd)]

def prompt_password():
    while True:
        pwd = input("Введіть пароль: ").strip()
        errors = validate(pwd)
        if not errors:
            print("✅ Пароль коректний!")
            return True
        print("❌ Не вийшло:")
        for e in errors:
            print("  •", e)
        if input("Ще раз? [y/N]: ").lower() != 'y':
            return False

def main():
    while True:
        print("\n1) Перевірити пароль\n2) Вийти")
        cmd = input("> ").strip()
        if cmd == '1':
            if prompt_password():
                break
        elif cmd == '2':
            break
        else:
            print("Невідомий вибір. Спробуйте 1 або 2.")

if __name__ == "__main__":
    main()