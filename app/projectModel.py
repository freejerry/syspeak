import datetime
from . import db

class Project(db.Model):
    __tablename__ = 'project'

    prj_id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(150))
    api_key = db.Column(db.String(200))
    created_time = db.Column(db.DateTime, default=datetime.datetime.now)
    creator = db.Column(db.Integer)

    def __init__(self, prj_id=None, name=None, description=None, api_key=None, created_time=None, creator=None):
        self.prj_id = prj_id
        self.name = name
        self.description = description
        self.api_key = api_key
        self.created_time = created_time
        self.creator = creator

    def __repr__(self):
        return '<Project %r>' % self.name

    def __str__(self):
        return '<Project %s>' % self.name