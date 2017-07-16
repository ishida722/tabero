import tabero.secret as secret

SQLALCHEMY_DATABASE_URI = 'sqlite:///tabero.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = secret.FLASK_SECRET_KEY
