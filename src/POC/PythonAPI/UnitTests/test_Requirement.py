from unittest import TestCase
from unittest.mock import patch
from PythonAPI.pythonapiPoC import Requirement
from flask import Response, Flask
from bson.json_util import dumps

app = Flask(__name__)


class TestRequirement(TestCase):
    @patch('PythonAPI.pythonapiPoC.db_insert_one')
    def test_post(self, mock):
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
        mock.return_value = return_value, 201
        # Set a local response as api expected output

        # Call the api with db_find mocked
        with app.test_request_context(method='POST', json=payload):
            api_response = Requirement.post()

        # Asserts
        self.assertEqual(api_response.status_code, 201)
        self.assertIsNotNone(mock.response)
        assert mock.call_count == 1

    @patch('PythonAPI.pythonapiPoC.db_find_one')
    def test_get(self, mock):
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
        mock.return_value = return_value, 200
        # Set a local response as api expected output

        # Call the api with db_find mocked
        with app.test_request_context('/requirement?_Id=5c82b45faf50340d8860f2ef'):
            api_response = Requirement.get()

        mock_response = Response(dumps(return_value), mimetype='application/json')

        # Asserts
        self.assertEqual(api_response.status_code, 200)
        self.assertIsNotNone(mock.response)
        assert mock.call_count == 1
        assert mock_response.data == api_response.data

    @patch('PythonAPI.pythonapiPoC.db_delete_one')
    def test_delete(self, mock):

        # Set the mocks return value
        mock.return_value = "", 204
        # Set a local response as api expected output

        # Call the api with db_find mocked
        with app.test_request_context('/requirement?_Id=5c82b45faf50340d8860f2ef'):
            api_response = Requirement.delete()

        mock_response = Response(dumps(""), mimetype='application/json')

        # Asserts
        self.assertEqual(api_response.status_code, 204)
        self.assertIsNotNone(mock.response)
        assert mock.call_count == 1
        assert mock_response.data == api_response.data

    @patch('PythonAPI.pythonapiPoC.db_replace_one')
    def test_put(self, mock):
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
        mock.return_value = payload, 204
        # Set a local response as api expected output

        # Call the api with db_find mocked
        with app.test_request_context(method='POST', json=payload):
            api_response = Requirement.put()

        # Asserts
        self.assertEqual(api_response.status_code, 204)
        self.assertIsNotNone(mock.response)
        assert mock.call_count == 1
