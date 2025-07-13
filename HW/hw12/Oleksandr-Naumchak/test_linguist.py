from linguist import *

# Test User creation
u1 = user_create("Alice", "alice@example.com", "pass123")
assert u1.name == "Alice"
assert u1.email == "alice@example.com"

# Test get user by id
assert user_get_by_id(u1.id) == u1

# Test update user name
user_update_name(u1.id, "Alicia")
assert user_get_by_id(u1.id).name == "Alicia"

# Test password change
assert user_change_password(u1.id, "pass123", "newpass")
assert not user_change_password(u1.id, "wrong", "fail")

# Test Deck creation
d1 = deck_create("Food", u1.id)
assert d1.name == "Food"
assert d1.user_id == u1.id

# Test get/update/delete deck
assert deck_get_by_id(d1.id) == d1
deck_update(d1.id, "Groceries")
assert deck_get_by_id(d1.id).name == "Groceries"
assert deck_delete_by_id(d1.id)
assert deck_get_by_id(d1.id) is None

# Test Card creation
c1 = card_create(u1.id, "apple", "яблуко", "fruit")
assert c1.word == "apple"
assert c1.translation == "яблуко"

# Test card filter
c2 = card_create(u1.id, "banana", "банан", "yellow fruit")
result = card_filter("fruit")
assert len(result) == 2

# Test card update
card_update(c1.id, word="grape")
assert card_get_by_id(c1.id).word == "grape"

# Test card delete
assert card_delete_by_id(c1.id)
assert card_get_by_id(c1.id) is None

print("✅ All tests passed.")