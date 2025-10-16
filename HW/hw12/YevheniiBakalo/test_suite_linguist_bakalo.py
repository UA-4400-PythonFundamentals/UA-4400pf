# test_suite_linguist_bakalo.py
# Unit tests for linguist_bakalo.py using unittest framework

import importlib
import unittest
import linguist_bakalo as M  # import my main module


# reloads module before each test to reset data
class FreshStateMixin:
    def setUp(self):
        importlib.reload(M)


# ======== USER TESTS ========
class TestUsers(FreshStateMixin, unittest.TestCase):
    def test_create_and_get(self):
        # check user creation and getting by id
        user = M.user_create("Eve", "eve@ex.com", "123")
        self.assertIsInstance(user, M.User)
        self.assertIs(M.user_get_by_id(user.id), user)

    def test_update_and_password(self):
        # check name update and password change
        u = M.user_create("Dan", "dan@ex.com", "pass")
        M.user_update_name(u.id, "Daniel")
        self.assertEqual(M.user_get_by_id(u.id).name, "Daniel")

        self.assertTrue(M.user_change_password(u.id, "pass", "new"))
        self.assertFalse(M.user_change_password(u.id, "wrong", "fail"))

    def test_delete_user(self):
        # check user deletion and repeated deletion
        u = M.user_create("Bob", "b@ex.com", "pw")
        self.assertTrue(M.user_delete_by_id(u.id))
        self.assertIsNone(M.user_get_by_id(u.id))
        self.assertFalse(M.user_delete_by_id(u.id))


# ======== DECK TESTS ========
class TestDecks(FreshStateMixin, unittest.TestCase):
    def test_deck_crud(self):
        # create, update and delete deck
        owner = M.user_create("Owner", "o@ex.com", "pw")
        d = M.deck_create("Languages", owner.id)
        self.assertIsInstance(d, M.Deck)

        M.deck_update(d.id, "Human Languages")
        self.assertEqual(M.deck_get_by_id(d.id).name, "Human Languages")

        self.assertTrue(M.deck_delete_by_id(d.id))
        self.assertIsNone(M.deck_get_by_id(d.id))


# ======== CARD TESTS ========
class TestCards(FreshStateMixin, unittest.TestCase):
    def test_create_and_filter(self):
        # create cards and test filter function
        u1 = M.user_create("Alice", "a@ex.com", "pw")
        u2 = M.user_create("Bob", "b@ex.com", "pw2")

        c1 = M.card_create(u1.id, "apple", "яблуко", "fruit")
        c2 = M.card_create(u1.id, "banana", "банан", "Yellow fruit")
        c3 = M.card_create(u2.id, "bread", "хліб", "bakery")

        self.assertIs(M.card_get_by_id(c1.id), c1)

        result = M.card_filter("fruit")
        self.assertEqual({x.id for x in result}, {c1.id, c2.id})

    def test_update_card(self):
        # check updating word, translation and tip
        u = M.user_create("C", "c@ex.com", "z")
        c = M.card_create(u.id, "table", "стіл", "furniture")

        M.card_update(c.id, word="desk")
        self.assertEqual(M.card_get_by_id(c.id).word, "desk")

        M.card_update(c.id, translation="парта")
        self.assertEqual(M.card_get_by_id(c.id).translation, "парта")

        prev_tip = M.card_get_by_id(c.id).tip
        M.card_update(c.id, tip=None)
        self.assertEqual(M.card_get_by_id(c.id).tip, prev_tip)

    def test_delete_card(self):
        # check card deletion and repeated deletion
        u = M.user_create("D", "d@ex.com", "w")
        c = M.card_create(u.id, "sun", "сонце", "space")

        self.assertTrue(M.card_delete_by_id(c.id))
        self.assertIsNone(M.card_get_by_id(c.id))
        self.assertFalse(M.card_delete_by_id(c.id))


# ======== SLOTS CHECK ========
class TestDataclassSlots(FreshStateMixin, unittest.TestCase):
    def test_slots_enforced(self):
        # make sure slots=True blocks new attributes
        u = M.user_create("Slots", "s@ex.com", "pw")
        with self.assertRaises(AttributeError):
            u.new_attr = 100


if __name__ == "__main__":
    unittest.main()
