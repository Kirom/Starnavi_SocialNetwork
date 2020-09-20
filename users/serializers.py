"""Auth's serializers."""
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, User

from rest_framework import serializers

from users.models import ExtendedUser


class UserSerializer(serializers.ModelSerializer):
    """Serializes user's model."""

    class Meta:
        """Defining metadata for group's model serializer."""

        model = User
        fields = ["id", "url", "username", "last_login", "email", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)


class ExtendedUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = ExtendedUser
        fields = ('user', 'last_activity',)

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of extended_user
        :return: returns a successfully created extended_user record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(),
                                     validated_data=user_data)
        extended_user, created = ExtendedUser.objects. \
            update_or_create(user=user)
        return extended_user


class GroupSerializer(serializers.ModelSerializer):
    """Serializes group's model."""

    class Meta:
        """Defining metadata for group's model serializer."""

        model = Group
        fields = ["url", "name"]
