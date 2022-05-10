from rest_framework.test import APITestCase
from django.urls import reverse


class TestViewsSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.refresh_url = reverse('refresh')

        self.user_data = {
            'first_name': "Milos",
            'last_name': "Nikic",
            'password': "Test",
            'confirm_password': "Test",
            'email': "milos.nikic@tnation.eu",
            'username': "milosnikic"
        }

        self.new_user_same_username  = {
            'first_name': "Ivan",
            'last_name': "Ivanovic",
            'password': "ivan",
            'confirm_password': "ivan",
            'email': "ivan.ivanovic@tnation.eu",
            'username': "milosnikic"
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

