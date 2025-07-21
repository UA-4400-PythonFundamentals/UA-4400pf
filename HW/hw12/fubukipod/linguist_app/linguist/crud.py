# linguist/crud.py

from .db import get_connection
from .models import User, Deck, Card

def user_create(name: str, email: str, password: str) -> User:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user (name, email, password) VALUES (?, ?, ?)",
        (name, email, password)
    )
    conn.commit()
    uid = cur.lastrowid
    return User(id=uid, name=name, email=email, password=password)

def user_get_by_id(user_id: int) -> User | None:
    conn = get_connection()
    row = conn.execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
    return User(**row) if row else None

def user_update_name(user_id: int, name: str) -> User | None:
    conn = get_connection()
    conn.execute("UPDATE user SET name = ? WHERE id = ?", (name, user_id))
    conn.commit()
    return user_get_by_id(user_id)

def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    u = user_get_by_id(user_id)
    if not u or u.password != old_password:
        return False
    conn = get_connection()
    conn.execute("UPDATE user SET password = ? WHERE id = ?", (new_password, user_id))
    conn.commit()
    return True

def user_delete_by_id(user_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM user WHERE id = ?", (user_id,))
    conn.commit()
    return cur.rowcount > 0

def deck_create(name: str, user_id: int) -> Deck:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO deck (name, user_id) VALUES (?, ?)", (name, user_id))
    conn.commit()
    did = cur.lastrowid
    return Deck(id=did, name=name, user_id=user_id)

def deck_get_by_id(deck_id: int) -> Deck | None:
    conn = get_connection()
    row = conn.execute("SELECT * FROM deck WHERE id = ?", (deck_id,)).fetchone()
    return Deck(**row) if row else None

def deck_update(deck_id: int, name: str) -> Deck | None:
    conn = get_connection()
    conn.execute("UPDATE deck SET name = ? WHERE id = ?", (name, deck_id))
    conn.commit()
    return deck_get_by_id(deck_id)

def deck_delete_by_id(deck_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM deck WHERE id = ?", (deck_id,))
    conn.commit()
    return cur.rowcount > 0

def card_create(user_id: int, word: str, translation: str, tip: str) -> Card:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO card (user_id, word, translation, tip) VALUES (?, ?, ?, ?)",
        (user_id, word, translation, tip)
    )
    conn.commit()
    cid = cur.lastrowid
    return Card(id=cid, user_id=user_id, word=word, translation=translation, tip=tip)

def card_get_by_id(card_id: int) -> Card | None:
    conn = get_connection()
    row = conn.execute("SELECT * FROM card WHERE id = ?", (card_id,)).fetchone()
    return Card(**row) if row else None

def card_filter(sub: str) -> tuple[Card, ...]:
    conn = get_connection()
    pattern = f"%{sub}%"
    rows = conn.execute(
        "SELECT * FROM card WHERE word LIKE ? OR translation LIKE ? OR tip LIKE ?",
        (pattern, pattern, pattern)
    ).fetchall()
    return tuple(Card(**r) for r in rows)

def card_update(card_id: int,
                word: str | None = None,
                translation: str | None = None,
                tip: str | None = None) -> Card | None:
    conn = get_connection()
    cur = conn.cursor()
    fields, vals = [], []
    if word is not None:
        fields.append("word = ?"); vals.append(word)
    if translation is not None:
        fields.append("translation = ?"); vals.append(translation)
    if tip is not None:
        fields.append("tip = ?"); vals.append(tip)
    if not fields:
        return card_get_by_id(card_id)
    vals.append(card_id)
    sql = f"UPDATE card SET {', '.join(fields)} WHERE id = ?"
    cur.execute(sql, vals)
    conn.commit()
    return card_get_by_id(card_id)

def card_delete_by_id(card_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM card WHERE id = ?", (card_id,))
    conn.commit()
    return cur.rowcount > 0

# ---- Додаткові “get_all” функції ----

def user_get_all() -> list[User]:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM user").fetchall()
    return [User(**r) for r in rows]

def deck_get_all() -> list[Deck]:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM deck").fetchall()
    return [Deck(**r) for r in rows]

def card_get_all() -> list[Card]:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM card").fetchall()
    return [Card(**r) for r in rows]
