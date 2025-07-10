import re

def has_lowercase(password):
    return bool(re.search(r"[a-z]", password))

def has_uppercase(password):
    return bool(re.search(r"[A-Z]", password))

def has_digit(password):
    return bool(re.search(r"\d", password))

def has_special_char(password):
    return bool(re.search(r"[$#@]", password))

def has_valid_length(password):
    return 6 <= len(password) <= 16