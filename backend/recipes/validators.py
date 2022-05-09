from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueValidator


def required(value):
    if value is None:
        raise ValidationError('This field is required')