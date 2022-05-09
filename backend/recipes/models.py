from django.db import models
from django.db.models import Avg

from api.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=500, null=True)

    REQUIRED_FIELDS = ['name']

    @property
    def average_rating(self):
        if hasattr(self, '_average_rating'):
            return self._average_rating

        rating = self.ratings.aggregate(Avg('rating'))['rating__avg']
        print(rating)
        if rating is None:
            rating = 0
        return  rating
            

class Rating(models.Model):
    rating = models.IntegerField(null=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='users')
    recipe = models.ForeignKey(Recipe, null=False, on_delete=models.CASCADE, related_name='ratings')