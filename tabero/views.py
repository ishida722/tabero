#coding:utf-8
import datetime
from flask import render_template, url_for
from flask_app import app, db
from tabero.models import Food
from tabero import tabero
import random

def AddFood():
    food = tabero.Tabetai()
    db.session.add(food)
    db.session.commit()

@app.route('/')
def LandingPage():
    return render_template('top.html')

@app.route('/tabetai')
def SuggestFood():
    food = tabero.Tabetai()
    return render_template('tabero.html', food=food)

@app.route('/foodlist/genarate')
def GenarateFoodList():
    AddFood()
    return "food list genarated"

@app.route('/foodlist')
def ShowFoodList():
    return str(Food.query.first())
