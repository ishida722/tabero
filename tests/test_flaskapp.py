from flask_app import app, db
from tabero import views
import unittest

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_root(self):
        rv = self.app.get('/')
