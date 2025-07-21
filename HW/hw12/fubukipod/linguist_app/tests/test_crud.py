# tests/test_crud.py
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from linguist.db import reset_db
from linguist.crud import (
    user_create, user_get_by_id, user_update_name,
    user_change_password, user_delete_by_id,
    deck_create, deck_get_by_id, deck_update, deck_delete_by_id,
    card_create, card_get_by_id, card_filter,
    card_update, card_delete_by_id
)

class CrudTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        
        reset_db()
        print("\n[Setup] In-memory database has been reset.\n")

    def test_user_crud(self):
        print(">> TEST: user_create")
        u = user_create("Olena", "olena@example.com", "1234")
        print("   -> Created User:", u)
        self.assertEqual(u.name, "Olena")

        print(">> TEST: user_get_by_id")
        fetched = user_get_by_id(u.id)
        print("   -> Retrieved User:", fetched)
        self.assertIsNotNone(fetched)

        print(">> TEST: user_update_name")
        updated = user_update_name(u.id, "Olena I.")
        print("   -> After update_name:", updated)
        self.assertEqual(updated.name, "Olena I.")

        print(">> TEST: user_change_password (fail case)")
        ok = user_change_password(u.id, "wrong", "x")
        print("   -> Change with wrong old:", ok)
        self.assertFalse(ok)

        print(">> TEST: user_change_password (success case)")
        ok2 = user_change_password(u.id, "1234", "x")
        print("   -> Change with correct old:", ok2)
        self.assertTrue(ok2)

        print(">> TEST: user_delete_by_id")
        deleted = user_delete_by_id(u.id)
        print("   -> Deleted:", deleted)
        self.assertTrue(deleted)
        self.assertIsNone(user_get_by_id(u.id))

    def test_deck_crud(self):
        print("\n>> TEST: deck_create")
        u = user_create("TestUser", "t@example.com", "pw")
        d = deck_create("D1", u.id)
        print("   -> Created Deck:", d)
        self.assertEqual(d.name, "D1")

        print(">> TEST: deck_get_by_id")
        fetched = deck_get_by_id(d.id)
        print("   -> Retrieved Deck:", fetched)
        self.assertIsNotNone(fetched)

        print(">> TEST: deck_update")
        upd = deck_update(d.id, "DD")
        print("   -> After update:", upd)
        self.assertEqual(upd.name, "DD")

        print(">> TEST: deck_delete_by_id")
        deleted = deck_delete_by_id(d.id)
        print("   -> Deleted:", deleted)
        self.assertTrue(deleted)
        self.assertIsNone(deck_get_by_id(d.id))

        user_delete_by_id(u.id)

    def test_card_crud(self):
        print("\n>> TEST: card_create")
        u = user_create("CardUser", "cu@example.com", "pw")
        c1 = card_create(u.id, "book", "книга", "read")
        c2 = card_create(u.id, "bookmark", "закладка", "hold")
        print("   -> Created Cards:", c1, "and", c2)
        self.assertNotEqual(c1.id, c2.id)

        print(">> TEST: card_get_by_id")
        fetched1 = card_get_by_id(c1.id)
        print("   -> Retrieved Card 1:", fetched1)
        self.assertEqual(fetched1.word, "book")

        print(">> TEST: card_filter")
        matches = card_filter("book")
        print(f"   -> card_filter('book') returned {len(matches)} cards:", matches)
        self.assertGreaterEqual(len(matches), 2)

        print(">> TEST: card_update")
        updated = card_update(c1.id, tip="newtip")
        print("   -> After update tip:", updated)
        self.assertEqual(updated.tip, "newtip")

        print(">> TEST: card_delete_by_id")
        deleted = card_delete_by_id(c2.id)
        print("   -> Deleted Card 2:", deleted)
        self.assertTrue(deleted)
        self.assertIsNone(card_get_by_id(c2.id))

        user_delete_by_id(u.id)

if __name__ == "__main__":
    unittest.main(buffer=False, verbosity=2)