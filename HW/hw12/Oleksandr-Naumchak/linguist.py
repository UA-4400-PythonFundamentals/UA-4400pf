from dataclasses import dataclass, field
from typing import Optional, List, Tuple

USERS: List['User'] = []
DECKS: List['Deck'] = []
CARDS: List['Card'] = []

user_id_counter = deck_id_counter = card_id_counter = 1

@dataclass
class User:
    id: int
    name: str
    email: str
    password: str

@dataclass
class Deck:
    id: int
    name: str
    user_id: int

@dataclass
class Card:
    id: int
    user_id: int
    word: str
    translation: str
    tip: str

def user_create(name, email, password) -> User:
    global user_id_counter
    user = User(user_id_counter, name, email, password)
    USERS.append(user)
    user_id_counter += 1
    return user

def user_get_by_id(user_id) -> Optional[User]:
    return next((u for u in USERS if u.id == user_id), None)

def user_update_name(user_id, name) -> Optional[User]:
    user = user_get_by_id(user_id)
    if user:
        user.name = name
    return user

def user_change_password(user_id, old_password, new_password) -> bool:
    user = user_get_by_id(user_id)
    if user and user.password == old_password:
        user.password = new_password
        return True
    return False

def user_delete_by_id(user_id) -> bool:
    global USERS
    user = user_get_by_id(user_id)
    if user:
        USERS = [u for u in USERS if u.id != user_id]
        return True
    return False

def deck_create(name, user_id) -> Deck:
    global deck_id_counter
    deck = Deck(deck_id_counter, name, user_id)
    DECKS.append(deck)
    deck_id_counter += 1
    return deck

def deck_get_by_id(deck_id) -> Optional[Deck]:
    return next((d for d in DECKS if d.id == deck_id), None)

def deck_update(deck_id, name) -> Optional[Deck]:
    deck = deck_get_by_id(deck_id)
    if deck:
        deck.name = name
    return deck

def deck_delete_by_id(deck_id) -> bool:
    global DECKS
    deck = deck_get_by_id(deck_id)
    if deck:
        DECKS = [d for d in DECKS if d.id != deck_id]
        return True
    return False

def card_create(user_id, word, translation, tip) -> Card:
    global card_id_counter
    card = Card(card_id_counter, user_id, word, translation, tip)
    CARDS.append(card)
    card_id_counter += 1
    return card

def card_get_by_id(card_id) -> Optional[Card]:
    return next((c for c in CARDS if c.id == card_id), None)

def card_filter(sub_word) -> Tuple[Card]:
    return tuple(c for c in CARDS if sub_word.lower() in c.word.lower() or
                 sub_word.lower() in c.translation.lower() or
                 sub_word.lower() in c.tip.lower())

def card_update(card_id, word=None, translation=None, tip=None) -> Optional[Card]:
    card = card_get_by_id(card_id)
    if card:
        if word is not None:
            card.word = word
        if translation is not None:
            card.translation = translation
        if tip is not None:
            card.tip = tip
    return card

def card_delete_by_id(card_id) -> bool:
    global CARDS
    card = card_get_by_id(card_id)
    if card:
        CARDS = [c for c in CARDS if c.id != card_id]
        return True
    return False