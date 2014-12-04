__author__ = 'manu'

from api import db


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(100), index=True, unique=True)
    room_id = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '<Room %r>' % self.room_name

