import pdb
from .test_setup import TestModelsSetup

from recipes.models import Rating


class TestModels(TestModelsSetup):
    def test_recipe_average_rating(self):
        rating1 = Rating.objects.create(rating=5, user=self.user1, recipe=self.recipe1)
        rating2 = Rating.objects.create(rating=1, user=self.user1, recipe=self.recipe1)

        self.recipe1.ratings.add(rating1, rating2)
        self.assertEqual(self.recipe1.average_rating, 3.0)
    
    def test_recipe_average_when_no_ratings(self):
        self.assertEqual(self.recipe1.average_rating, 0)