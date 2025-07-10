# Import necessary modules for password hashing
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """
    User model for a Flask application (in-memory demonstration).

    This model defines the structure of a User object without direct database
    integration using an ORM like SQLAlchemy. It's suitable for simple
    in-memory examples or as a base if you plan to integrate with a different
    data storage mechanism manually (e.g., a custom file-based system,
    or a different database driver).
    """

    # A simple in-memory "database" for demonstration purposes.
    # In a real application, this would be replaced by a proper database.
    _users_data = {}
    _next_id = 1

    def __init__(self, username, password):
        """
        Initializes a new User instance.
        Assigns a unique ID and hashes the provided password.
        """
        self.id = User._next_id
        User._next_id += 1
        self.username = username
        self.password_hash = self._set_password(password) # Call internal method to hash password
        User._users_data[self.id] = self # Add self to in-memory store

    def __repr__(self):
        """
        String representation of the User object.
        Useful for debugging and logging.
        """
        return f'<User {self.username}>'

    def _set_password(self, password):
        """
        Hashes the provided password and returns the hash.
        Used internally during initialization.
        """
        return generate_password_hash(password)

    def check_password(self, password):
        """
        Checks if the provided password matches the stored password hash.
        Uses werkzeug.security.check_password_hash for secure comparison.
        Returns True if passwords match, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_all(cls):
        print(cls._users_data.values())
        return cls._users_data.values()
    @classmethod
    def find_by_username(cls, username):
        """
        Class method to find a user by username from the in-memory store.
        """
        for user_id, user in cls._users_data.items():
            if user.username == username:
                return user
        return None

    @classmethod
    def get(cls, user_id):
        """
        Class method to get a user by ID from the in-memory store.
        """
        return cls._users_data.get(user_id)

    @classmethod
    def add_user(cls, username, password):
        """
        Adds a new user to the in-memory store.
        Returns the created User object.
        """
        if cls.find_by_username(username):
            return None # User already exists
        new_user = cls(username, password)
        return new_user

    @classmethod
    def generate_dummy_users(cls, num_users):
        """
        Generates a specified number of dummy users and adds them to the in-memory store.
        Usernames will be 'dummy_user_1', 'dummy_user_2', etc., with a generic password.
        """
        generated_users = []
        for i in range(1, num_users + 1):
            username = f'dummy_user_{i}'
            password = 'password123' # A simple password for dummy users
            if not cls.find_by_username(username): # Only add if username doesn't exist
                new_user = cls(username, password)
                generated_users.append(new_user)
        return generated_users