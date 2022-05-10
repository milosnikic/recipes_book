from rest_framework import serializers

from django.core.exceptions import ObjectDoesNotExist

from .models import Ingridient
from recipes.validators import required
from .validators import unique_name_validator


class IngridientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[required, unique_name_validator])
    number_of_recipes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ingridient
        fields = [
            "id",
            "name",
            "number_of_recipes",
        ]

class IngridientSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field)
        except (TypeError, ValueError):
            self.fail('invalid')