from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Count


User = get_user_model() 

# Create your models here.
class Workshop(models.Model):
    skills_choices = (
        ("python", "Python"),
        ("django", "Django"),
        ("react", "React"),
        ("javascript", "JavaScript"),
        ("htmlcss", "HTML/CSS"),
    )
    skills = models.CharField(
        max_length=100,
        choices=skills_choices,
        default=None,
        blank=False, 
        null=True, ## if django breaks change this to False
    )
    title = models.CharField(
        max_length=200,
    )
    workshop_date = models.DateTimeField()
    description = models.TextField()
    image = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    is_open = models.BooleanField()
    # current_mentor_num = models.IntegerField()
    max_mentor_num = models.IntegerField()

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="workshop_owner",
    ) 
    
## attempting to make current_mentor_count work

# class WorkshopSignups(models.Model):
#     workshops = models.ForeignKey(
#         Workshop,
#         on_delete=models.CASCADE,
#         related_name="current_mentor_num"
#     )
#     mentor = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="current_mentor_num"
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         unique_together = ('workshops', 'mentor')

#     current_mentor_num = mentor.objects.count()