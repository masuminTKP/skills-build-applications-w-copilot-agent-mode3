from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            "email": "testuser@example.com",
            "name": "Test User",
            "age": 25
        }

    def test_create_user(self):
        response = self.client.post("/api/users/", self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        self.client.post("/api/users/", self.user_data)
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
