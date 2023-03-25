from rest_framework import serializers
from .models import User


# class SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Skill
#         fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    # skills = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    username = serializers.EmailField()
    is_python_mentor = serializers.BooleanField()
    is_django_mentor = serializers.BooleanField()
    is_react_mentor = serializers.BooleanField()
    is_javascript_mentor = serializers.BooleanField()
    is_htmlcss_mentor = serializers.BooleanField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'skills', 'password', 'is_python_mentor', 'is_django_mentor', 'is_react_mentor', 'is_javascript_mentor', 'is_htmlcss_mentor'
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
        instance.is_python_mentor = validated_data.get(
            'is_python_mentor', instance.is_python_mentor)
        instance.is_django_mentor = validated_data.get(
            'is_django_mentor', instance.is_django_mentor)
        instance.is_react_mentor = validated_data.get(
            'is_react_mentor', instance.is_react_mentor)
        instance.is_javascript_mentor = validated_data.get(
            'is_javascript_mentor', instance.is_javascript_mentor)
        instance.is_htmlcss_mentor = validated_data.get(
            'is_htmlcss_mentor', instance.is_htmlcss_mentor)
        instance.save()
        return instance
