# linguist/cli.py

import sys
from .crud import (
    user_create, user_get_by_id, user_get_all,
    deck_create, deck_get_by_id, deck_get_all,
    card_create, card_filter, card_get_all
)
from .seed import seed_data

MENU = """
1) Seed sample data
2) Створити нового користувача
3) Показати користувача за ID
4) Показати всіх користувачів
5) Створити колоду
6) Показати колоду за ID
7) Показати всі колоди
8) Створити картку
9) Пошук карток (за підрядком)
10) Показати всі картки
0) Вихід
"""

def main():
    while True:
        print(MENU)
        choice = input("Вибір> ").strip()
        if choice == "0":
            sys.exit()
        elif choice == "1":
            seed_data()
            print("✅ База наповнена прикладами.")
        elif choice == "2":
            name = input("Ім'я: ")
            email = input("Email: ")
            pwd = input("Пароль: ")
            u = user_create(name, email, pwd)
            print("Створено:", u)
        elif choice == "3":
            uid = int(input("User ID: "))
            print(user_get_by_id(uid) or "Не знайдено.")
        elif choice == "4":
            users = user_get_all()
            if users:
                for u in users:
                    print(" •", u)
            else:
                print("Користувачів немає.")
        elif choice == "5":
            uid = int(input("User ID: "))
            name = input("Назва колоди: ")
            d = deck_create(name, uid)
            print("Створено:", d)
        elif choice == "6":
            did = int(input("Deck ID: "))
            print(deck_get_by_id(did) or "Не знайдено.")
        elif choice == "7":
            decks = deck_get_all()
            if decks:
                for d in decks:
                    print(" •", d)
            else:
                print("Колод немає.")
        elif choice == "8":
            uid   = int(input("User ID: "))
            word  = input("Word (EN): ")
            tr    = input("Translation (UA): ")
            tip   = input("Tip: ")
            c = card_create(uid, word, tr, tip)
            print("Створено:", c)
        elif choice == "9":
            sub = input("Підрядок для пошуку: ")
            found = card_filter(sub)
            if found:
                for c in found:
                    print(" •", c)
            else:
                print("Нічого не знайдено.")
        elif choice == "10":
            cards = card_get_all()
            if cards:
                for c in cards:
                    print(" •", c)
            else:
                print("Карток немає.")
        else:
            print("Невідомий вибір.")

if __name__ == "__main__":
    main()
