from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=300)
    first_name = serializers.CharField(max_length=300)
    last_name = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=1000)
    skills = serializers.CharField(max_length=100)

    # class Skill(serializers.TextChoices):
    #     PY = "Python"
    #     DJ = "Django"
    #     RE = "React"
    #     JS = "JavaScript"
    #     HT = "HTML/CSS"

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
