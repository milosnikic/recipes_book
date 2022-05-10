from django.db import models


class Ingridient(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)


    @property
    def number_of_recipes(self):
        if hasattr(self, '_number_of_recipes'):
            return self._number_of_recipes
        return self.recipes.count

    def __str__(self):
        return self.name