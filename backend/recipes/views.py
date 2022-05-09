from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Recipe
from .serializers import RecipeSerializer

class RecipesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
