from check.rules import (
    has_lowercase,
    has_uppercase,
    has_digit,
    has_special_char,
    has_valid_length
)

def is_valid_password(password):
    return (
        has_lowercase(password) and
        has_uppercase(password) and
        has_digit(password) and
        has_special_char(password) and
        has_valid_length(password)
    )