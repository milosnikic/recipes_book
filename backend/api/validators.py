from rest_framework.validators import UniqueValidator

from .models import User


unique_validator = UniqueValidator(queryset=User.objects.all(), lookup='iexact')