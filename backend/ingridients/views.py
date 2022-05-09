from rest_framework import generics

from recipes.mixins import IsAuthenticatedMixin
from .models import Ingridient
from .serializers import IngridientSerializer


class IngridientsListCreateAPIView(
        IsAuthenticatedMixin,
        generics.ListCreateAPIView):
    queryset = Ingridient.objects.all()
    serializer_class = IngridientSerializer
