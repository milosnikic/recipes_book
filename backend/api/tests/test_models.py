from django.test import TestCase

from api.models import User

class TestModels(TestCase):
    def setUp(self) :
        User.objects.create(
            first_name="Milos",
            last_name="Nikic",
            email="milos.nikic@gmail.com",
            password="Test",
            username="milosnikic",
        )
    
    def test_user_username(self):
        user = User.objects.get(first_name="Milos")
        self.assertEqual(user.username, "milosnikic")