from rest_framework import serializers

from .models import Recipe
from .validators import required


# class RatingInlineSerializer(serializers.Serializer):
#     rating = serializers.DecimalField(
#         max_digits=3, decimal_places=2, read_only=True)
#     number_of_votes = serializers.IntegerField(read_only=True)


class RecipeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[required])
    average_rating = serializers.DecimalField(max_digits=4, decimal_places=2, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            "pk",
            "name",
            "text",
            "average_rating"
        ]
