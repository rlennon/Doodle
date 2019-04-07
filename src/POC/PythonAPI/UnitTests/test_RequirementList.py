from unittest import TestCase
from unittest.mock import patch, Mock


class TestRequirementList(TestCase):
    @patch('PythonAPI.pythonapiPoC.RequirementList')
    def test_get(self, mock_get):
        req = mock_get()

        req.posts.return_value = [
            {
                "_id": {
                    "$oid": "5c82b45faf50340d8860f2ef"
                },
                "height": "3",
                "length": "20",
                "name": "Doodle",
                "lan connections": "16",
                "width": "25"
            },
            {
                "name": "Store Room 3",
                "_id": {
                    "$oid": "5c8ce80d3173c017fa744b4a"
                },
                "height": "3",
                "length": "20",
                "width": "10"
            },
            {
                "_id": {
                    "$oid": "5c8ce8803173c0181a7d67c8"
                },
                "height": "3",
                "length": "20",
                "name": "Store Room 10",
                "lan connections": "16",
                "width": "14"
            },
            {
                "name": "Store Room 6",
                "_id": {
                    "$oid": "5c8ceb623173c018f498c9e5"
                },
                "height": "3",
                "length": "20",
                "width": "10"
            },
            {
                "name": "Store Room 7",
                "_id": {
                    "$oid": "5c8cebfd3173c0192305f3ed"
                },
                "height": "3",
                "length": "20",
                "width": "10"
            },
            {
                "name": "Store Room 8",
                "_id": {
                    "$oid": "5c8fc5403173c02ad5fd0981"
                },
                "height": "3",
                "length": "20",
                "width": "10"
            },
            {
                "width": "11",
                "height": "2",
                "length": "12",
                "name": "Store Room 99",
                "_id": {
                    "$oid": "5c94fc703173c00c5a972128"
                },
                "new field": "Test"
            },
            {
                "width": "11",
                "height": "2",
                "length": "12",
                "name": "Store Room 99",
                "_id": {
                    "$oid": "5c94fc7e3173c00c5a972129"
                },
                "new field": "Test"
            }
        ]

        response = req.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)



