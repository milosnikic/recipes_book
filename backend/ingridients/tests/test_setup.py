from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse

from ingridients.models import Ingridient
from recipes.models import Recipe
from api.models import User


class TestViewsSetup(APITestCase):
    def setUp(self) -> None:
        self.list_or_create_url = reverse('list-ingridients')
        self.most_used_url = reverse('list-most-used-ingridients')

        self.user = User.objects.create(
            first_name="Milos",
            last_name="Nikic",
            password="Test",
            email="milos.nikic@tnation.eu",
            username="milosnikic"
        )

        self.client.force_authenticate(user=self.user)

        self.ingridient1 = Ingridient.objects.create(name="Milk")
        self.ingridient2 = Ingridient.objects.create(name="Flour")
        self.ingridient3 = Ingridient.objects.create(name="Water")
        self.ingridient4 = Ingridient.objects.create(name="Oil")
        self.ingridient5 = Ingridient.objects.create(name="Eggs")

        self.recipe1 = Recipe.objects.create(
            name="Pancake", text="Simple pancakes", user=self.user)
        self.recipe2 = Recipe.objects.create(
            name="Eggs", text="Best eggs", user=self.user)
        self.recipe3 = Recipe.objects.create(
            name="Bread", text="White bread", user=self.user)

        self.recipe1.ingridients.add(
            self.ingridient1, self.ingridient2, self.ingridient3, self.ingridient4, self.ingridient5)
        self.recipe2.ingridients.add(self.ingridient4, self.ingridient5)
        self.recipe3.ingridients.add(self.ingridient5)

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()


class TestModelsSetup(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            first_name="Milos",
            last_name="Nikic",
            password="Test",
            email="milos.nikic@tnation.eu",
            username="milosnikic"
        )

        self.ingridient1 = Ingridient.objects.create(name="Milk")
        self.ingridient2 = Ingridient.objects.create(name="Flour")
        self.ingridient3 = Ingridient.objects.create(name="Water")
        self.ingridient4 = Ingridient.objects.create(name="Oil")
        self.ingridient5 = Ingridient.objects.create(name="Eggs")

        self.recipe1 = Recipe.objects.create(
            name="Pancake", text="Simple pancakes", user=self.user)
        self.recipe2 = Recipe.objects.create(
            name="Eggs", text="Best eggs", user=self.user)
        self.recipe3 = Recipe.objects.create(
            name="Bread", text="White bread", user=self.user)

        self.recipe1.ingridients.add(
            self.ingridient1, self.ingridient2, self.ingridient3, self.ingridient4, self.ingridient5)
        self.recipe2.ingridients.add(self.ingridient4, self.ingridient5)
        self.recipe3.ingridients.add(self.ingridient5)

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
