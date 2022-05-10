from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg
from django.db.models.functions import Coalesce
from .models import Recipe


class IsAuthenticatedMixin():
    permission_classes = [IsAuthenticated]


class UserQuerySetMixin():
    user_field = 'user'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user

        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup_data)


class RecipeSearchMixin():
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        min = self.request.GET.get('min')
        max = self.request.GET.get('max')
        if q is not None or min is not None or max is not None:
            return qs.search(q, min, max)
        return Recipe.objects.all().annotate(_average_rating=Coalesce(Avg('ratings__rating'), 0.0))
