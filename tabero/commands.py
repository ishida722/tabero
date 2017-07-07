from flask_app import db

def init():
    db.create_all()
