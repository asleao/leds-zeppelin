from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.state import User

from users.api.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """Handle creating, reading and updating User"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
