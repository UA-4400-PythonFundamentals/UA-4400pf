# linguist/seed.py

from .crud import user_create, deck_create, card_create

def seed_data():
    u = user_create("Ivan", "ivan@example.com", "secret")
    deck = deck_create("Basics", u.id)
    card_create(u.id, "apple", "яблуко", "Think of Newton")
    card_create(u.id, "apply", "застосовувати", "Use in code")
