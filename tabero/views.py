#coding:utf-8
import datetime
from flask import render_template, url_for
from flask_app import app, db
from tabero.models import Food
from tabero import tabero
import random
import os

@app.route('/')
def LandingPage():
    return render_template('top.html')

@app.route('/tabetai')
def SuggestFood():
    food = Food.query.order_by(Food.time).first()
    return render_template('tabero.html', food=food)

@app.route('/foodlist/genarate')
def GenarateFoodList():
    Food.query.delete()
    foods = tabero.Tabetai()
    for food in foods:
        db.session.add(Food(food))
    db.session.commit()
    return 'foodlist genarated'

@app.route('/foodlist')
def ShowFoodList():
    return str(Food.query.all())

@app.route('/foodlist/init')
def DataBaseInit():
    if os.path.exists('tabero.db'):
        os.remove('tabero.db')
    db.create_all()
