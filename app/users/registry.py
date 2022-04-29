from app.db import interface
from app.users.user import User

# Entity use case
class Users():
    def __init__(self, db: interface.DB):
        self.db = db

    def new(self, name: str, email: str):
        # Validation here, probably.
        user = User(name, email)
        self.db.new(user)
