#coding:utf-8
import datetime
from flask import render_template, url_for
from tabero.flask_app import app, db
from tabero.models import Food
from tabero.tabero import Tabero
import random

tabe = Tabero()

def DeleteAlpha():
    notFoods = Food.query.filter(str(Food.name).isalnum()==True)
    for food in notFoods:
        db.session.delete(food)
    db.session.commit()

def AddFood():
    for food in tabe.FetchFoodList():
        newFood = Food(str(food))
        db.session.add(newFood)
    db.session.commit()

def DeleteOutdatedFood(lifeTime):
    outdateFoods = Food.query.filter(Food.time < (datetime.datetime.now() - datetime.timedelta(seconds=lifeTime)))
    for food in outdateFoods:
        db.session.delete(food)
    db.session.commit()

@app.route('/')
def LandingPage():
    return render_template('top.html')

@app.route('/tabetai')
def SuggestFood():
    food = str(random.choice(Food.query.all()))
    return render_template('tabero.html', food=food)

@app.route('/foodlist/genarate')
def GenarateFoodList():
    AddFood()
    # DeleteOutdatedFood(300)
    # DeleteAlpha()
    return "food list genarated"

@app.route('/foodlist/fetch')
def FetchFood():
    return str(tabe.FetchFoodList())

@app.route('/foodlist')
def ShowFoodList():
    return str(Food.query.first())
