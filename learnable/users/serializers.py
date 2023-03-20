from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.EmailField()
    first_name = serializers.CharField(max_length=300)
    last_name = serializers.CharField(max_length=300)
    password = serializers.CharField(max_length=1000)

    skills_choices = (
        ("python", "Python"),
        ("django", "Django"),
        ("react", "React"),
        ("javascript", "JavaScript"),
        ("htmlcss", "HTML/CSS"),
    )
    skills = serializers.MultipleChoiceField(choices=skills_choices)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserDetailSerializer(UserSerializer):
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance 
