from rest_framework import serializers
from .models import Workshop 

class WorkshopSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    workshop_date = serializers.DateTimeField()
    description = serializers.CharField(max_length=None)
    image = serializers.URLField()
    created_at = serializers.DateTimeField(read_only=True)
    is_open = serializers.BooleanField()
    # mentor_num = serializers.IntegerField()
    current_mentor_num = serializers.ReadOnlyField()
    max_mentor_num = serializers.IntegerField()
    skills_choices = (
        ("python", "Python"),
        ("django", "Django"),
        ("react", "React"),
        ("javascript", "JavaScript"),
        ("htmlcss", "HTML/CSS"),
    )
    skills = serializers.ChoiceField(choices=skills_choices) ##check skill's max length with what Bunny has
    ### multipleChoiceField(choices=skills_choices) OR choiceField
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self,validated_data):
        return Workshop.objects.create(**validated_data)

# class WorkshopDetailSerializer(serializers.Serializer):
class WorkshopDetailSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.workshop_date = validated_data.get('workshop_date', instance.workshop_date)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.current_mentor_num = validated_data.get('current_mentor_num', instance.current_mentor_num)
        instance.max_mentor_num = validated_data.get('max_mentor_num', instance.max_mentor_num)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
 