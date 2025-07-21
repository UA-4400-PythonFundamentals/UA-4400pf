# linguist/models.py

from dataclasses import dataclass

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
