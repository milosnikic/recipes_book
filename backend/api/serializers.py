from rest_framework import serializers


from .models import User
from . import validators

from .clearbit import get_additional_user_data


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[validators.unique_validator, validators.email_validator])
    username = serializers.CharField(validators=[validators.unique_validator])
    class Meta:
        model = User
        fields = ['id',
                  'first_name',
                  'last_name',
                  'username',
                  'email',
                  'password',
                  'confirm_password',
                  ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username']
        )

        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords have to match!'})
        
        (location, github, linkedin) = get_additional_user_data(self.validated_data['email'])

        user.location = location
        user.github = github
        user.linkedin = linkedin

        user.set_password(password)
        user.save()
        return user
