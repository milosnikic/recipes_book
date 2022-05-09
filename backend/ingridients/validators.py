from rest_framework.validators import UniqueValidator
from .models import Ingridient


unique_name_validator = UniqueValidator(queryset=Ingridient.objects.all(), lookup='iexact')