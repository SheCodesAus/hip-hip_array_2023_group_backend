from django.db import models
# from django.contrib.auth import User

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
    current_mentor_num = models.IntegerField(
        default = 0
    )
    max_mentor_num = models.IntegerField()

    '''align with Bunny's user.app to do the below'''
    # owner_id = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name="workshop_owner",
    # )
