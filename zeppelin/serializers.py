from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'username', 'email', 'name', 'matricula', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            matricula=validated_data['matricula']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
