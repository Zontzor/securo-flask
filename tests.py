# tests.py
# Run with python 'tests.py'

import unittest
import os

from flask import abort, url_for
from flask_testing import TestCase

from app import create_app, db
from app.models import User, Photo

class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql://alex:test12345@localhost/securo_test'
        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test user
        user = User(username="alex", password="test12345", is_admin=True)

        # save users to database
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestModels(TestBase):

    def test_user_model(self):
        """
        Test number of records in User table
        """
        self.assertEqual(User.query.count(), 1)

if __name__ == '__main__':
    unittest.main()
