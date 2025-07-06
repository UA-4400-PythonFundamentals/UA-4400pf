from loger_config import logger

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        logger.info(f"User created: {self.username}")

    def update_password(self, new_password: str):
        logger.info(f"Password for user {self.username} updated.")
        self.password = new_password

    def __repr__(self):
        return f"User(username={self.username})"

    def __str__(self):
        return f"User: {self.username}"
    
