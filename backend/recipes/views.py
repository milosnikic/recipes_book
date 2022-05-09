from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django.db.models import Avg
from django.db.models.functions import Coalesce

from .models import Recipe
from .serializers import RecipeSerializer


class RecipesListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Recipe.objects.all().annotate(_average_rating=Coalesce(Avg('ratings__rating'), 0.0))