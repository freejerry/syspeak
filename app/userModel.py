from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    user_id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(25), unique=True, index=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(10))

    projects = db.relationship("Project", backref=db.backref("user"))

    def __init__(self, user_id=None, account=None, password=None, name="anonymous"):
        self.user_id = user_id
        self.account = account
        self.password = password
        self.name = name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return '<User %r>' % self.name

    def __str__(self):
        return '<User %s>' % self.name