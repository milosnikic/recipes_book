from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse

from ingridients.models import Ingridient
from recipes.models import Rating, Recipe
from api.models import User


class TestViewsSetup(APITestCase):
    def setUp(self) -> None:
        self.list_or_create_url = reverse('recipe-list')
        self.own_list_url = reverse('recipe-own-list')
        self.detail_url = reverse('recipe-detail', args=['3'])
        self.rate_url = reverse('recipe-rate')

        self.user1 = User.objects.create(
            first_name="Milos",
            last_name="Nikic",
            password="Test",
            email="milos.nikic@tnation.eu",
            username="milosnikic"
        )

        self.user2 = User.objects.create(
            first_name="Goran",
            last_name="Medenica",
            password="Test",
            email="goran.medenica@tnation.eu",
            username="goranmedenica"
        )

        self.recipe_data = {
            "name": "Test Recipe",
            "text": "This is a test recipe",
            "ingridients": [
                "Milk",
                "Flour"
            ],
        }

        self.invalid_recipe_id_rate_data = {'rating': 5, 'recipe_id': 1}
        self.less_than_one_data = {'rating':-1, 'recipe_id': 1}
        self.greater_than_five_data = {'rating':6, 'recipe_id': 1}

        self.client.force_authenticate(user=self.user1)

        self.ingridient1 = Ingridient.objects.create(name="Milk")
        self.ingridient2 = Ingridient.objects.create(name="Flour")
        self.ingridient3 = Ingridient.objects.create(name="Water")
        self.ingridient4 = Ingridient.objects.create(name="Oil")
        self.ingridient5 = Ingridient.objects.create(name="Eggs")

        self.recipe1 = Recipe.objects.create(
            name="Pancake", text="Simple pancakes", user=self.user1)
        self.recipe2 = Recipe.objects.create(
            name="Eggs", text="Best eggs", user=self.user1)
        self.recipe3 = Recipe.objects.create(
            name="Bread", text="White bread", user=self.user2)

        self.recipe1.ingridients.add(
            self.ingridient1, self.ingridient2, self.ingridient3, self.ingridient4, self.ingridient5)
        self.recipe2.ingridients.add(self.ingridient4, self.ingridient5)
        self.recipe3.ingridients.add(self.ingridient5)

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()


class TestModelsSetup(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(
            first_name="Milos",
            last_name="Nikic",
            password="Test",
            email="milos.nikic@tnation.eu",
            username="milosnikic"
        )

        self.recipe1 = Recipe.objects.create(
            name="Pancake", text="Simple pancakes", user=self.user1)
        

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()