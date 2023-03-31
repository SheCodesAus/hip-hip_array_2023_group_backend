from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

# Create your models here.
class Workshop(models.Model):
    '''DONE - align the attribute names in 'skills' with Bunny's names'''
    # skills_choices = (
    #     ("python", "Python"),
    #     ("django", "Django"),
    #     ("react", "React"),
    #     ("javascript", "JavaScript"),
    #     ("htmlcss", "HTML/CSS"),
    # )
    # skills = models.CharField(
    #     max_length=100,
    #     choices=skills_choices,
    #     default=None,
    #     blank=False, 
    #     null=True, ## if django breaks change this to False
    # )
    is_python_mentor = models.BooleanField(default=False)
    is_django_mentor = models.BooleanField(default=False)
    is_react_mentor = models.BooleanField(default=False)
    is_javascript_mentor = models.BooleanField(default=False)
    is_htmlcss_mentor = models.BooleanField(default=False)
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
    current_mentor_num = models.ManyToManyField(
        User,
        related_name='mentor_counter'
    )
  
  # @property
    # def current_mentor_num(self):
    #     return self.workshop.objects.aggregate(Count('mentor_num'))

    # @current_mentor_num.setter
    # def current_mentor_num(self, value):
    #     pass