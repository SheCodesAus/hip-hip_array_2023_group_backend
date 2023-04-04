from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Workshop
from django.contrib.auth import get_user_model

User = get_user_model() 

class WorkshopSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    workshop_date = serializers.DateTimeField()
    description = serializers.CharField(max_length=None)
    image = serializers.URLField()
    created_at = serializers.DateTimeField(read_only=True)
    is_open = serializers.BooleanField()
    max_mentor_num = serializers.IntegerField()
    is_python_mentor = serializers.BooleanField(default=False)
    is_django_mentor = serializers.BooleanField(default=False)
    is_react_mentor = serializers.BooleanField(default=False)
    is_javascript_mentor = serializers.BooleanField(default=False)
    is_htmlcss_mentor = serializers.BooleanField(default=False)
    owner = serializers.IntegerField(read_only=True,source='user.id')
    mentors = UserSerializer(read_only=True,many=True)
    mentor_count = serializers.IntegerField(read_only=True)
    def create(self,validated_data):
        return Workshop.objects.create(**validated_data)

class WorkshopDetailSerializer(WorkshopSerializer):
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.workshop_date = validated_data.get('workshop_date', instance.workshop_date)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.max_mentor_num = validated_data.get('max_mentor_num', instance.max_mentor_num)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.mentors = validated_data.get('current_mentor_num', instance.current_mentor_num)
        instance.save()
        return instance
 