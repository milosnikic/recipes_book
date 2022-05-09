from rest_framework.permissions import IsAuthenticated


class IsAuthenticatedMixin():
    permission_classes = [IsAuthenticated]


class UserQuerySetMixin():
    user_field = 'user'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user

        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup_data)