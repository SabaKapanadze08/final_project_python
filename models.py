from ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class services_item(db.Model):

    __tablename__ = "services_items"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Integer())
    image = db.Column(db.String())


class ContactMessage(db.Model):

    __tablename__ = "contact_messages"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(80))
    message = db.Column(db.String(400))

class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(80))
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    role = db.Column(db.String())

    def __init__(self, email, username, password, role="Guest"):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)    


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Review(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    author_name = db.Column(db.String(100))
    author_initials = db.Column(db.String(10))
    rating = db.Column(db.Integer())
    message = db.Column(db.String())
    date = db.Column(db.DateTime(), default=datetime.utcnow)