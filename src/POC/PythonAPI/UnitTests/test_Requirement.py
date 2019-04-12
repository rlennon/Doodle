from unittest import TestCase
from unittest.mock import patch


class TestRequirement(TestCase):
    @patch('PythonAPI.pythonapiPoC.Requirement')
    def test_post(self, mock_post):
        req = mock_post()

        req.posts.return_value = {
            "$oid": "5cafc78e3173c020055db522"
        }

        response = req.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)

    @patch('PythonAPI.pythonapiPoC.Requirement')
    def test_get(self, mock_get):
        req = mock_get()

        req.posts.return_value = {
            "_id": {
                "$oid": "5c8ce8803173c0181a7d67c8"
            },
            "width": "14",
            "name": "Store Room 10",
            "height": "3",
            "length": "20",
            "lan connections": "16"
        }

        response = req.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)

    @patch('PythonAPI.pythonapiPoC.Requirement')
    def test_delete(self, mock_delete):
        req = mock_delete()

        response = req.posts()
        response.status_code = 204
        self.assertIsNotNone(response)

    @patch('PythonAPI.pythonapiPoC.Requirement')
    def test_put(self, mock_put):
        req = mock_put()

        response = req.posts()
        response.status_code = 204
        self.assertIsNotNone(response)
