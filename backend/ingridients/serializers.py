from rest_framework import serializers

from .models import Ingridient
from recipes.validators import required
from .validators import unique_name_validator


class IngridientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[required, unique_name_validator])

    class Meta:
        model = Ingridient
        fields = [
            "id",
            "name",
        ]
