from loger_config import logger
from .user import User

def generate_users(num_users: int):
    logger.info(f"Generating {num_users} users.")
    users = []
    for i in range(num_users):
        user = User(username=f"user{i}", password=f"pass{i}")
        users.append(user)
        logger.info(f"Generated user: {user}")
    return users