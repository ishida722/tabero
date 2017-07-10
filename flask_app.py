# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create our little application :)

app = Flask(__name__)
app.config.from_object('tabero.config')

db = SQLAlchemy(app)

import tabero.views
