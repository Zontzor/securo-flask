# tests.py

# Run with 'python tests.py'

import unittest
import os
import json

from app import create_app, db

class TestBase(unittest.TestCase):

    def setUp(self):
        """
        Define test variables and initialize app
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

    def test_photo_creation(self):
        """
        Test API creation of a photo (POST request)
        """
        res = self.client().post('/photos/', data=self.photo)
        self.assertEqual(res.status_code, 201)
        self.assertIn('20170901090000', str(res.data))

    def test_api_can_get_all_photos(self):
        """
        Test API can get a photo (GET request)
        """
        res = self.client().post('/photos/', data=self.photo)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/photos/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('20170901090000', str(res.data))

    def test_api_can_get_photo_by_id(self):
        """
        Test API can get a single photo by using it's id
        """
        rv = self.client().post('/photos/', data=self.photo)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/photos/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('20170901090000', str(result.data))

    def test_photo_can_be_edited(self):
        """
        Test API can edit an existing photo (PUT request)
        """
        rv = self.client().post(
            '/photos/',
            data={'filename': '10160901090000'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/photos/1',
            data={
                "filename": "20160901090000"
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/photos/1')
        self.assertIn('2016', str(results.data))

    def test_photo_deletion(self):
        """
        Test API can delete an existing photo. (DELETE)
        """
        rv = self.client().post(
            '/photos/',
            data={'filename': '10160901090000'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/photos/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/photos/1')
        self.assertEqual(result.status_code, 404)

if __name__ == '__main__':
    unittest.main()
