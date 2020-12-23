from flask_pymongo import PyMongo
from flask_login import LoginManager, current_user
import bcrypt

mongo = PyMongo()

login_manager = LoginManager()


class User:
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    @staticmethod
    def is_admin():
        return mongo.db.users.find_one({'username':current_user.get_id()})['admin']

    def get_id(self):
        return self.username

    @staticmethod
    def check_password(password_hash, password):
        return bcrypt.checkpw(password, password_hash)