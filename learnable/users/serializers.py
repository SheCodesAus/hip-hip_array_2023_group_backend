from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_python_mentor",
            "is_django_mentor",
            "is_react_mentor",
            "is_javascript_mentor",
            "is_htmlcss_mentor",
        ]
        id = serializers.ReadOnlyField()

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserDetailSerializer(UserSerializer):
    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.password = validated_data.get("password", instance.password)
        instance.is_python_mentor = validated_data.get(
            "is_python_mentor", instance.is_python_mentor
        )
        instance.is_django_mentor = validated_data.get(
            "is_django_mentor", instance.is_django_mentor
        )
        instance.is_react_mentor = validated_data.get(
            "is_react_mentor", instance.is_react_mentor
        )
        instance.is_javascript_mentor = validated_data.get(
            "is_javascript_mentor", instance.is_javascript_mentor
        )
        instance.is_htmlcss_mentor = validated_data.get(
            "is_htmlcss_mentor", instance.is_htmlcss_mentor
        )
        instance.save()
        return instance
