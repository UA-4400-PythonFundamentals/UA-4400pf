import re




def valid_password(password: str) -> bool:
    pattern = r'^(?=.*[@#$])(?=.*[A-Z])(?=.*[a-z])((?=.*[0-9])).{6,16}$'
    return bool(re.fullmatch(pattern, password))