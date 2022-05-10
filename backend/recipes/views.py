from rest_framework import generics

from recipes.mixins import IsAuthenticatedMixin, UserQuerySetMixin

from .models import Recipe
from .serializers import RecipeSerializer, RatingCreateSerializer
from .mixins import RecipeSearchMixin


class RecipesOwnListAPIView(
        UserQuerySetMixin,
        IsAuthenticatedMixin,
        RecipeSearchMixin,
        generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipesListCreateAPIView(
        IsAuthenticatedMixin,
        RecipeSearchMixin,
        generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecipeRetrieveAPIView(
        IsAuthenticatedMixin,
        generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RatingCreateAPIView(
        IsAuthenticatedMixin,
        generics.CreateAPIView):
    serializer_class = RatingCreateSerializer
