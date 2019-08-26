from datetime import datetime
from . import db


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(
        db.String(30),
        index=True,
        primary_key=True)
    deck_json = db.Column(db.String(300), nullable=False)
    rotate_direction = db.Column(db.Integer, nullable=True, default=1)
    field_top = db.Column(db.String(30), nullable=False)
    turn_event = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'Room(id={self.id}, rotate_direction={self.rotate_direction}, field_top={self.field_top}, turn_event={self.turn_event})'


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(
        db.String(30),
        index=True,
        primary_key=True)
    room_id = db.Column(
        db.String(30),
        db.ForeignKey(
            'rooms.id', ondelete="CASCADE"))
    room = db.relationship(
        "Room", primaryjoin="Room.id == User.room_id", uselist=False, lazy="join")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)


    def __repr__(self):
        return f'User(id={self.id}, room_id={self.room_id}, created_at={self.created_at})'
