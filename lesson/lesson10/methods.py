class User:
    _count = 0
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        User._count += 1

    def rename(self, new_name):
        """Rename the User."""
        self.name = new_name
    def __str__(self):
        return f"{self.name} ({self.age}), Email: {self.email}"
    
    @classmethod
    def count(cls):
        return cls._count
    
    @staticmethod
    def create(name, age, email):
        """Create a new User instance."""
        return User(name, age, email)
    
a = User("Alice", 30, " test@test.com")
print(a)  # Output: Alice (30), Email:
a.rename("Alice Smith")
print(a)  # Output: Alice Smith (30), Email:
# User.rename("Alice Johnson")#TypeError: User.rename() missing 1 required positional argument: 'new_name'
User.rename(a, "Alice Johnson")
print(a)  # Output: Alice Johnson (30), Email:
print(User.count())  # Output: 1
print(a.count())  # Output: {'name': 'Alice Johnson', 'age': 30, 'email': '
print(User.create("Bob", 25, ""))
print(a.create("Bob", 25, ""))