from rest_framework.serializers import ValidationError


def required(value):
    if value is None:
        raise ValidationError('This field is required')