from djoser.serializers import UserCreateSerializer

from apps.users.models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        )
