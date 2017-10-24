# tests.py

# Run with 'python tests.py'

import unittest
import os
import json

from app import create_app, db

class TestBase(unittest.TestCase):

    def setUp(self):
        """
        Will be called before every test
        """
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.photo = {'filename': '20170901090000'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def tearDown(self):
        """
        Will be called after every test
        """
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

if __name__ == '__main__':
    unittest.main()
