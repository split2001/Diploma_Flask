from sqlalchemy import ForeignKey
from db import db
from models.word import Word
from models.user import User

class UserWord(db.Model):
    __tablename__= 'user_word'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    word_id = db.Column(db.Integer, ForeignKey('word.id'))
    is_learned = db.Column(db.Boolean, default=False, nullable=False)

    word = db.relationship('Word', back_populates='users')
    user  = db.relationship('User', back_populates='words')