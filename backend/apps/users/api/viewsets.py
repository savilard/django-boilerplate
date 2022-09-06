from djoser.views import UserViewSet as DjoserUserViewSet


from apps.users.models import CustomUser


class UserViewSet(DjoserUserViewSet):
    """ViewSet пользователя."""

    queryset = CustomUser.objects.all()
