from flask_app import app
from tabero import views
import unittest
import os
from html.parser import HTMLParser
from flask_sqlalchemy import SQLAlchemy
from tabero.models import Food

class Parser(HTMLParser):
    def handle_data(self, data):
        print(data)

    def handle_starttag(self, tag, attrs):
        print('{},{}'.format(tag, attrs))

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        Food.query.delete()

    def tearDown(self):
        Food.query.delete()

    def IsHttpOk(self, rv):
        self.assertEqual(200, rv.status_code)

    def test_root(self):
        rv = self.app.get('/')
        self.IsHttpOk(rv)
        self.assertTrue('Tabero' in str(rv.data))

    def test_NoneTabetai(self):
        rv = self.app.get('/tabetai')
        self.IsHttpOk(rv)
        self.assertTrue('None 食べろ' in str(rv.data, encoding='utf-8'))

    @unittest.skip('late')
    def test_Tabetai(self):
        self.app.get('/foodlist/genarate')
        rv = self.app.get('/tabetai')
        self.IsHttpOk(rv)
        self.assertFalse('None 食べろ' in str(rv.data, encoding='utf-8'))

    def test_NoneFoodList(self):
        rv = self.app.get('/foodlist')
        self.IsHttpOk(rv)
        self.assertEqual('[]', str(rv.data, encoding='utf-8'))

    @unittest.skip('late')
    def test_GenarateFoodList(self):
        rv = self.app.get('/foodlist/genarate')
        self.IsHttpOk(rv)
        self.assertEqual('foodlist genarated', str(rv.data, encoding='utf-8'))
        self.assertNotEqual('[]', str(rv.data, encoding='utf-8'))
