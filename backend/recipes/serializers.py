from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import Recipe, Rating
from api.models import User
from .validators import required


class RatingCreateSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
    user_id = serializers.IntegerField(validators=[required], write_only=True)
    recipe_id = serializers.IntegerField(validators=[required], write_only=True)

    class Meta:
        model = Rating
        fields = [
            'pk',
            'rating',
            'user_id',
            'recipe_id',
        ]

    def save(self):
        rating = Rating(rating=self.validated_data['rating'])

        user_id = self.validated_data['user_id']
        recipe_id = self.validated_data['recipe_id']

        user = User.objects.filter(pk=user_id).first()
        recipe = Recipe.objects.filter(pk=recipe_id).first()
        if user is None or recipe is None:
            raise ValidationError(
                {'message': 'Please make sure you pass valid user/recipe ids'})
        rating.user = user
        rating.recipe = recipe
        rating.save()
        return rating


class RecipeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[required])
    average_rating = serializers.DecimalField(
        max_digits=4, decimal_places=2, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            "pk",
            "name",
            "text",
            "average_rating"
        ]
