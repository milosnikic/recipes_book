from cgitb import lookup
from django.db import models
from django.db.models import Avg, Q, Count

from api.models import User
from ingridients.models import Ingridient


class RecipeQuerySet(models.QuerySet):
    def search(self, query, min, max):
        if self.has_only_query(query, min, max):
            lookup = Q(name__icontains=query) | Q(text__icontains=query) | Q(ingridients__name__icontains=query)
            return self.filter(lookup)
        qs = self.annotate(number_of_ingridients=Count('ingridients__id'))
        lookup = Q(name__icontains=query) | Q(text__icontains=query) | Q(ingridients__name__icontains=query) if query is not None else Q()
        min_lookup = Q(number_of_ingridients__gte=int(min)) if min is not None else Q()
        max_lookup = Q(number_of_ingridients__lte=int(max)) if max is not None else Q()
        qs = qs.filter(lookup).filter(min_lookup).filter(max_lookup)
        return qs

    def has_only_query(self, query, min, max):
        return min is None and max is None and query is not None


class RecipeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return RecipeQuerySet(self.model, using=self.db)

    def search(self, query, min=None, max=None):
        return self.get_queryset().search(query, min, max)


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(User, default=3, null=False,
                             on_delete=models.CASCADE, related_name='recipes')
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
    user = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name='ratings')
    recipe = models.ForeignKey(
        Recipe, null=False, on_delete=models.CASCADE, related_name='ratings')
