from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import Recipe, Rating
from api.models import User
from .validators import required


class UserInlineSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
        ]


class RatingCreateSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
    recipe_id = serializers.IntegerField(
        validators=[required], write_only=True)
    user = UserInlineSerializer(read_only=True)

    class Meta:
        model=Rating
        fields=[
            "pk",
            "rating",
            "user",
            "recipe_id",
        ]

    def save(self):
        rating = Rating(rating=self.validated_data['rating'])

        request = self.context.get('request')
        user = request.user

        recipe_id = self.validated_data['recipe_id']
        recipe = Recipe.objects.filter(pk=recipe_id).first()
        if recipe is None:
            raise ValidationError(
                {'message': 'Please make sure you pass valid recipe id'})
        if recipe.user == user:
            raise ValidationError(
                {'message': 'You are not able to rate your own recipes'}
            )

        rating.recipe = recipe
        rating.user = user
        rating.save()
        return rating


class RecipeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[required])
    average_rating = serializers.DecimalField(
        max_digits=4, decimal_places=2, read_only=True)
    user = UserInlineSerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = [
            "pk",
            "user",
            "name",
            "text",
            "average_rating"
        ]
