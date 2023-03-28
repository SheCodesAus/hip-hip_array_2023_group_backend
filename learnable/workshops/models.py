from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model() 

# Create your models here.
class Workshop(models.Model):
    '''DONE - align the attribute names in 'skills' with Bunny's names'''
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
    current_mentor_num = models.IntegerField()
    max_mentor_num = models.IntegerField()

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="workshop_owner",
    ) 

    # class WorkshopMentor(models.Model):
    #     workshop_mentor = models.ManyToManyField('users_mentor')
     

  # @property
    # def current_mentor_num(self):
    #     return self.workshop.objects.aggregate(Count('mentor_num'))

    # @current_mentor_num.setter
    # def current_mentor_num(self, value):
    #     pass