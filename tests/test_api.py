import unittest
from fastapi.testclient import TestClient
from api import app


class TestCalculatorAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_add(self):
        response = self.client.post("/add", json={"a": 1, "b": 2})
        self.assertEqual(response.json()["result"], 3)

    def test_subtract(self):
        response = self.client.post("/subtract", json={"a": 6, "b": 4})
        self.assertEqual(response.json()["result"], 2)


if __name__ == "__main__":
    unittest.main()
