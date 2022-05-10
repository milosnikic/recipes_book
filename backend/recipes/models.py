from cgitb import lookup
from django.db import models
from django.db.models import Avg, Q

from api.models import User
from ingridients.models import Ingridient


class RecipeQuerySet(models.QuerySet):
    def search(self, query):
        lookup = Q(name__icontains=query) | Q(text__icontains=query) | Q(ingridients__name__icontains=query)
        qs = self.filter(lookup)
        return qs


class RecipeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return RecipeQuerySet(self.model, using=self.db)

    def search(self, query):
        return self.get_queryset().search(query)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(User, default=3, null=False, on_delete=models.CASCADE, related_name='recipes')
    ingridients = models.ManyToManyField(Ingridient, related_name="recipes")

    REQUIRED_FIELDS = ['name']

    objects = RecipeManager()

    @property
    def average_rating(self):
        if hasattr(self, '_average_rating'):
            return self._average_rating

        rating = self.ratings.aggregate(Avg('rating'))['rating__avg']
        if rating is None:
            rating = 0
        return rating
            

class Rating(models.Model):
    rating = models.IntegerField(null=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='ratings')
    recipe = models.ForeignKey(Recipe, null=False, on_delete=models.CASCADE, related_name='ratings')