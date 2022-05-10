from rest_framework import generics
from django.db.models import Count

from recipes.mixins import IsAuthenticatedMixin
from .models import Ingridient
from .serializers import IngridientSerializer


class IngridientsListCreateAPIView(
        IsAuthenticatedMixin,
        generics.ListCreateAPIView):
    queryset = Ingridient.objects.all()
    serializer_class = IngridientSerializer


class IngridientsMostUsedListAPIView(
        IsAuthenticatedMixin,
        generics.ListAPIView):
    serializer_class = IngridientSerializer

    def get_queryset(self):
        return Ingridient.objects.all().annotate(_number_of_recipes=Count("recipes"))\
            .order_by("-_number_of_recipes")\
            .filter(_number_of_recipes__gt=0)[:5]
