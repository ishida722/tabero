#coding:utf-8
import datetime
from tabero.flask_app import db

class Food(db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    time = db.Column(db.DateTime)

    def __init__(self, name):
        self.name = name
        self.time = datetime.datetime.today()

    def __repr__(self):
        return str(self.name)

def init():
    db.create_all()
