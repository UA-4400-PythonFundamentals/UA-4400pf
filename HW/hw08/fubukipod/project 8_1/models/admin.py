__all__ = ['create_admin']
from utils.logger import log_in_file
from utils.formatter import format_string

def create_admin(name: str):
    msg = format_string(f"Creating admin: {name}", 'red')
    print(msg)
    log_in_file(f"Admin created: {name}")
    return {'name': name, 'role': 'admin'}
