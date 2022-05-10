from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueValidator

from .models import User
from .hunter import verify_email

unique_validator = UniqueValidator(
    queryset=User.objects.all(), lookup='iexact')


def email_validator(value):
    if not verify_email(value):
        raise ValidationError(
            'Email is not valid according to hunter.io'
        )
