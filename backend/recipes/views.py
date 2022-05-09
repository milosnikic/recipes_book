from rest_framework import generics

from django.db.models import Avg
from django.db.models.functions import Coalesce

from recipes.mixins import IsAuthenticatedMixin

from .models import Recipe
from .serializers import RecipeSerializer, RatingCreateSerializer


class RecipesListCreateAPIView(
        IsAuthenticatedMixin,
        generics.ListCreateAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return Recipe.objects.all().annotate(_average_rating=Coalesce(Avg('ratings__rating'), 0.0))
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecipeRetrieveAPIView(
        IsAuthenticatedMixin,
        generics.RetrieveAPIView):
    serializer_class = RecipeSerializer
    
    def get_queryset(self):
        return Recipe.objects.all()

class RatingCreateAPIView(
        IsAuthenticatedMixin,
        generics.CreateAPIView):
    serializer_class = RatingCreateSerializer
