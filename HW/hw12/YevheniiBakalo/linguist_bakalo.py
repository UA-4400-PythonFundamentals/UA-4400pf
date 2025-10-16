from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Tuple
from itertools import count

USERS: List["User"] = []
DECKS: List["Deck"] = []
CARDS: List["Card"] = []

_user_ids = count(1)
_deck_ids = count(1)
_card_ids = count(1)

@dataclass(slots=True)
class User:
    id: int
    name: str
    email: str
    password: str

@dataclass(slots=True)
class Deck:
    id: int
    name: str
    user_id: int

@dataclass(slots=True)
class Card:
    id: int
    user_id: int
    word: str
    translation: str
    tip: str

def _pop_by_id(lst, _id) -> bool:
    for i, obj in enumerate(lst):
        if getattr(obj, "id", None) == _id:
            lst.pop(i)
            return True
    return False

def _first_by_id(lst, _id):
    for obj in lst:
        if getattr(obj, "id", None) == _id:
            return obj
    return None

def user_create(name, email, password) -> User:
    uid = next(_user_ids)
    u = User(uid, name, email, password)
    USERS.append(u)
    return u

def user_get_by_id(user_id) -> Optional[User]:
    return _first_by_id(USERS, user_id)

def user_update_name(user_id, name) -> Optional[User]:
    u = user_get_by_id(user_id)
    if u:
        u.name = name
    return u

def user_change_password(user_id, old_password, new_password) -> bool:
    u = user_get_by_id(user_id)
    if not u:
        return False
    if u.password != old_password:
        return False
    u.password = new_password
    return True

def user_delete_by_id(user_id) -> bool:
    return _pop_by_id(USERS, user_id)

def deck_create(name, user_id) -> Deck:
    did = next(_deck_ids)
    d = Deck(did, name, user_id)
    DECKS.append(d)
    return d

def deck_get_by_id(deck_id) -> Optional[Deck]:
    return _first_by_id(DECKS, deck_id)

def deck_update(deck_id, name) -> Optional[Deck]:
    d = deck_get_by_id(deck_id)
    if d:
        d.name = name
    return d

def deck_delete_by_id(deck_id) -> bool:
    return _pop_by_id(DECKS, deck_id)

def card_create(user_id, word, translation, tip) -> Card:
    cid = next(_card_ids)
    c = Card(cid, user_id, word, translation, tip)
    CARDS.append(c)
    return c

def card_get_by_id(card_id) -> Optional[Card]:
    return _first_by_id(CARDS, card_id)

def card_filter(sub_word) -> Tuple[Card, ...]:
    q = (sub_word or "").lower()
    result = [
        c for c in CARDS
        if q in c.word.lower() or q in c.translation.lower() or q in c.tip.lower()
    ]
    return tuple(result)

def card_update(card_id, word=None, translation=None, tip=None) -> Optional[Card]:
    c = card_get_by_id(card_id)
    if not c:
        return None
    if word is not None:
        c.word = word
    if translation is not None:
        c.translation = translation
    if tip is not None:
        c.tip = tip
    return c

def card_delete_by_id(card_id) -> bool:
    return _pop_by_id(CARDS, card_id)
