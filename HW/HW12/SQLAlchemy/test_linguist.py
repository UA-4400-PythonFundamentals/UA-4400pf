from linguist import User, Deck, Card

# Create user
user1 = User.user_create("Alice", "alice@email.com", "secret123")
assert user1.name == "Alice"
assert user1.email == "alice@email.com"
assert user1.password == "secret123"

# Get user by id
fetched = User.user_get_by_id(user1.id)
assert fetched is user1

# Update user name
updated = User.user_update_name(user1.id, "Alice Cooper")
assert updated.name == "Alice Cooper"

# Change password (success)
assert User.user_change_password(user1.id, "secret123", "newpass456") is True
assert user1.password == "newpass456"

# Change password (fail)
assert User.user_change_password(user1.id, "wrong_old_pass", "nope") is False

# Delete user
assert User.user_delete_by_id(user1.id) is True
assert User.user_get_by_id(user1.id) is None

# --- DECK TESTS ---
user2 = User.user_create("Bob", "bob@email.com", "pw")
deck1 = Deck.deck_create("Animals", user2.id)
assert deck1.name == "Animals"
assert deck1.user_id == user2.id

deck2 = Deck.deck_create("Colors", user2.id)
fetched_deck = Deck.deck_get_by_id(deck1.id)
assert fetched_deck is deck1

# Update deck name
Deck.deck_update(deck1.id, "Wild Animals")
assert deck1.name == "Wild Animals"

# Delete deck
assert Deck.deck_delete_by_id(deck2.id) is True
assert Deck.deck_get_by_id(deck2.id) is None

# --- CARD TESTS ---
card1 = Card.card_create(user2.id, "cat", "кіт", "Picture a cat in a hat")
assert card1.word == "cat"
assert card1.translation == "кіт"
assert card1.tip == "Picture a cat in a hat"

card2 = Card.card_create(user2.id, "dog", "пес", "Dog goes woof")
card3 = Card.card_create(user2.id, "blue", "синій", "Blue like the sky")

# Get card by id
fetched_card = Card.card_get_by_id(card2.id)
assert fetched_card is card2

# Filter cards
results = Card.card_filter("cat")
assert card1 in results
assert card2 not in results

results2 = Card.card_filter("woof")
assert card2 in results2

# Update card
Card.card_update(card1.id, translation="кішка", tip="Think of the word 'kitten'")
assert card1.translation == "кішка"
assert card1.tip == "Think of the word 'kitten'"

Card.card_update(card3.id, word="azure")
assert card3.word == "azure"

# Delete card
assert Card.card_delete_by_id(card2.id) is True
assert Card.card_get_by_id(card2.id) is None

print("All tests passed!")