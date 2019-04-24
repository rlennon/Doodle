from unittest import TestCase
from unittest.mock import patch
from api import RequirementList
from flask import Response
from bson.json_util import dumps


class TestRequirementList(TestCase):
    @patch('api.db_find')
    def test_get(self, mock):
        return_value = [
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

        # Set the mocks return value
        mock.return_value = return_value, 200
        # Set a local response as api expected output
        api_response = Response(dumps(return_value), mimetype='application/json')

        # Call the api with db_find mocked
        response = RequirementList.get()

        # Asserts
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response)
        assert mock.call_count == 1
        assert response.data == api_response.data


