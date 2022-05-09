from rest_framework import serializers

from .models import Recipe
from .validators import required


class RecipeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[required])
    class Meta:
        model = Recipe
        fields = [
            "pk",
            "name",
            "text"
        ]