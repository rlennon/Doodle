from unittest import TestCase
from unittest.mock import patch
from services.api import Requirement, db_find, db_find_one, db_insert_one, db_delete_one, db_replace_one
from flask import Response, Flask
from bson.json_util import dumps
import mock, pymongo

app = Flask(__name__)


class TestRequirement(TestCase):
    @patch('services.api.db_insert_one')
    def test_post(self, mock_post):
        new_id = "5cafc78e3173c020055db522"
        payload = {
            "width": "11",
            "name": "Store Room 99",
            "length": "12",
            "height": "2"
        }

        return_value = {
            "$oid": new_id
        }

        # Set the mocks return value
        mock_post.return_value = return_value, 201
        # Set a local response as api expected output

        # Call the api with db_find mocked
        with app.test_request_context(method='POST', json=payload):
            api_response = Requirement.post()

        # Asserts
        self.assertEqual(api_response.status_code, 201)
        self.assertIsNotNone(mock_post.response)
        assert mock_post.call_count == 1

    @patch('services.api.db_find_one')
    def test_get(self, mock_get):
        return_value = {
            "_id": {
                "$oid": "5c8ce8803173c0181a7d67c8"
            },
            "width": "14",
            "name": "Store Room 10",
            "height": "3",
            "length": "20",
            "lan connections": "16"
        }

        # Set the mocks return value
        mock_get.return_value = return_value, 200
        # Set a local response as api expected output

        # Call the api with db_find mocked
        with app.test_request_context('/requirement?_Id=5c82b45faf50340d8860f2ef'):
            api_response = Requirement.get()

        mock_response = Response(dumps(return_value), mimetype='application/json')

        # Asserts
        self.assertEqual(api_response.status_code, 200)
        self.assertIsNotNone(mock_get.response)
        assert mock_get.call_count == 1
        assert mock_response.data == api_response.data

    @patch('services.api.db_delete_one')
    def test_delete(self, mock_delete):

        # Set the mocks return value
        mock_delete.return_value = "", 204
        # Set a local response as api expected output

        # Call the api with db_find mocked
        with app.test_request_context('/requirement?_Id=5c82b45faf50340d8860f2ef'):
            api_response = Requirement.delete()

        mock_response = Response(dumps(""), mimetype='application/json')

        # Asserts
        self.assertEqual(api_response.status_code, 204)
        self.assertIsNotNone(mock_delete.response)
        assert mock_delete.call_count == 1
        assert mock_response.data == api_response.data

    @patch('services.api.db_replace_one')
    def test_put(self, mock_put):
        payload = {
            "name": "Store Room 10",
            "_id": {
                "$oid": "5c8ce8803173c0181a7d67c8"
            },
            "width": "14",
            "length": "20",
            "height": "3",
            "lan connections":    "16"
        }

        # Set the mocks return value
        mock_put.return_value = payload, 204
        # Set a local response as api expected output

        # Call the api with db_find mocked
        with app.test_request_context(method='POST', json=payload):
            api_response = Requirement.put()

        # Asserts
        self.assertEqual(api_response.status_code, 204)
        self.assertIsNotNone(mock_put.response)
        assert mock_put.call_count == 1

    @mock.patch('pymongo.collection.Collection.find')
    def test_db_find(self, mock_find):
        mock_find.return_value = [
            {
                "_id": {
                    "$oid": "5c82b45faf50340d8860f2ef"
                },
                "lan connections": "16",
                "height": "3",
                "length": "20",
                "width": "25",
                "name": "Doodle"
            },
            {
                "_id": {
                    "$oid": "5c8ce80d3173c017fa744b4a"
                },
                "length": "20",
                "name": "Store Room 3",
                "height": "3",
                "width": "10"
            }
        ]

        docs, status = db_find()
        assert status == 200
        assert docs is not None
        assert mock_find.call_count == 1

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_db_find_one(self, mock_find_one):
        mock_find_one.return_value = {
                "_id": {
                    "$oid": "5c82b45faf50340d8860f2ef"
                },
                "lan connections": "16",
                "height": "3",
                "length": "20",
                "width": "25",
                "name": "Doodle"
            }

        docs, status = db_find_one("5c8ce8803173c0181a7d67c8")
        assert status == 200
        assert docs is not None
        assert mock_find_one.call_count == 1

    @mock.patch('pymongo.collection.Collection.insert_one')
    def test_db_insert_one(self, mock_insert_one):

        docs, status = db_insert_one("5c8ce8803173c0181a7d67c8")
        assert status == 201
        assert mock_insert_one.call_count == 1

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_db_delete_one(self, mock_delete_one):

        docs, status = db_delete_one("5c8ce8803173c0181a7d67c8")
        assert status == 500
        assert docs is not None
        assert mock_delete_one.call_count == 1

    @mock.patch('pymongo.collection.Collection.replace_one')
    def test_db_replace_one(self, mock_replace_one):
        payload = {
            "name": "Store Room 10",
            "width": "14",
            "length": "20",
            "height": "3",
            "lan connections": "16"
        }
        docs, status = db_replace_one("5c8ce8803173c0181a7d67c8", payload)
        assert status == 500
        assert docs is not None
        assert mock_replace_one.call_count == 1

