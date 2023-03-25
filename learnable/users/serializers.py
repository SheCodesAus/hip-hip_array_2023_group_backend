from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField()
    # is_python_mentor = serializers.BooleanField(default=False)
    # is_django_mentor = serializers.BooleanField(default=False)
    # is_react_mentor = serializers.BooleanField()
    # is_javascript_mentor = serializers.BooleanField()
    # is_htmlcss_mentor = serializers.BooleanField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'password', 'is_python_mentor', 'is_django_mentor', 'is_react_mentor', 'is_javascript_mentor', 'is_htmlcss_mentor'
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserDetailSerializer(UserSerializer):
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
