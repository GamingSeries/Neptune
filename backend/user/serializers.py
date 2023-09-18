from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer as BaseUserSerializer,\
     UserCreateSerializer as BaseUserCreateSerializer

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']
