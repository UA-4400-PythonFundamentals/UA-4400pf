from typing import Optional, Tuple, List

class User:
    _users = {}
    _id_counter = 1

    def __init__(self, name: str, email: str, password: str):
        self.id = User._id_counter
        self.name = name
        self.email = email
        self.password = password
        User._users[self.id] = self
        User._id_counter += 1

    @staticmethod
    def user_create(name: str, email: str, password: str) -> "User":
        """
        Creates a new user and returns the User object.
        """
        return User(name, email, password)

    @staticmethod
    def user_get_by_id(user_id: int) -> Optional["User"]:
        """
        Retrieves a user by their ID and returns the User object.
        """
        return User._users.get(user_id)

    @staticmethod
    def user_update_name(user_id: int, name: str) -> Optional["User"]:
        """
        Updates the name of a user and returns the User object.
        """
        user = User._users.get(user_id)
        if user:
            user.name = name
        return user

    @staticmethod
    def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
        """
        Changes the password of a user and returns a Boolean value indicating success or failure.
        """
        user = User._users.get(user_id)
        if user and user.password == old_password:
            user.password = new_password
            return True
        return False

    @staticmethod
    def user_delete_by_id(user_id: int) -> bool:
        """
        Deletes a user by their ID and returns a Boolean value indicating success or failure.
        """
        if user_id in User._users:
            del User._users[user_id]
            return True
        return False


class Deck:
    _decks = {}
    _id_counter = 1

    def __init__(self, name: str, user_id: int):
        self.id = Deck._id_counter
        self.name = name
        self.user_id = user_id
        Deck._decks[self.id] = self
        Deck._id_counter += 1

    @staticmethod
    def deck_create(name: str, user_id: int) -> "Deck":
        """
        Creates a new deck belonging to a user and returns the Deck object.
        """
        return Deck(name, user_id)

    @staticmethod
    def deck_get_by_id(deck_id: int) -> Optional["Deck"]:
        """
        Retrieves a deck by its ID and returns the Deck object.
        """
        return Deck._decks.get(deck_id)

    @staticmethod
    def deck_update(deck_id: int, name: str) -> Optional["Deck"]:
        """
        Updates the name of a deck and returns the Deck object.
        """
        deck = Deck._decks.get(deck_id)
        if deck:
            deck.name = name
        return deck

    @staticmethod
    def deck_delete_by_id(deck_id: int) -> bool:
        """
        Deletes a deck by its ID and returns a Boolean value indicating success or failure.
        """
        if deck_id in Deck._decks:
            del Deck._decks[deck_id]
            return True
        return False


class Card:
    _cards = {}
    _id_counter = 1

    def __init__(self, user_id: int, word: str, translation: str, tip: str):
        self.id = Card._id_counter
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip
        Card._cards[self.id] = self
        Card._id_counter += 1

    @staticmethod
    def card_create(user_id: int, word: str, translation: str, tip: str) -> "Card":
        """
        Creates a new flashcard and returns the Card object.
        """
        return Card(user_id, word, translation, tip)

    @staticmethod
    def card_get_by_id(card_id: int) -> Optional["Card"]:
        """
        Retrieves a flashcard by its ID and returns the Card object.
        """
        return Card._cards.get(card_id)

    @staticmethod
    def card_filter(sub_word: str) -> Tuple["Card", ...]:
        """
        Retrieves all flashcards containing a substring in either the word, translation, or tip fields and returns a tuple of Card objects.
        """
        results = []
        for card in Card._cards.values():
            if (sub_word.lower() in card.word.lower() or
                sub_word.lower() in card.translation.lower() or
                sub_word.lower() in card.tip.lower()):
                results.append(card)
        return tuple(results)

    @staticmethod
    def card_update(card_id: int, word: Optional[str] = None, translation: Optional[str] = None, tip: Optional[str] = None) -> Optional["Card"]:
        """
        Updates the fields of a flashcard and returns the Card object.
        """
        card = Card._cards.get(card_id)
        if card:
            if word is not None:
                card.word = word
            if translation is not None:
                card.translation = translation
            if tip is not None:
                card.tip = tip
        return card

    @staticmethod
    def card_delete_by_id(card_id: int) -> bool:
        """
        Deletes a flashcard by its ID and returns a Boolean value indicating success or failure.
        """
        if card_id in Card._cards:
            del Card._cards[card_id]
            return True
        return False