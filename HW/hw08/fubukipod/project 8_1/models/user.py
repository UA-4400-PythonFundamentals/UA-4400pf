__all__ = ['create_user']
from utils.logger import log_in_file
from utils.formatter import format_string

def create_user(name: str):
    msg = format_string(f"Creating user: {name}", 'blue')
    print(msg)
    log_in_file(f"User created: {name}")
    return {'name': name, 'role': 'user'}
