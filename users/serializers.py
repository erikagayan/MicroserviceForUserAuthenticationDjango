from typing import Any, Dict
from users.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}  # No password return in JSON

    @staticmethod
    def validate_password(value):
        validate_password(value)
        return value

    def create(self, validated_data) -> User:
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

    def update(self, instance: User, validated_data) -> User:
        # Extracts password, removes it from dictionary
        password = validated_data.pop("password", None)

        # Remaining keys and values
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Check password
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
