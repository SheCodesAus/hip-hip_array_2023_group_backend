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
    current_mentor_num = serializers.IntegerField()
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
    owner = serializers.CharField(max_length=200) ##check owner's max length with what Bunny has

    def create(self,validated_data):
        return Workshop.objects.create(**validated_data)

# class WorkshopDetailSerializer(serializers.Serializer):
