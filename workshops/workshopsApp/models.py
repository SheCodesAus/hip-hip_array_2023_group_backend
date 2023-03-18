from django.db import models

# Create your models here.
class Workshop(models.Model):

    '''align the attribute names in 'skills' with Bunny's names'''
    class Skills(models.TextChoices):
        Python = "Python"
        Django = "Django"
        React = "React"
        JavaScript = "JavaScript"
        HTML_CSS = "HTML_&_CSS"
    skills = models.CharField(
        max_length=20,
        choices=Skills.choices,
    )
    title = models.CharField(
        max_length=200,
    )
    workshop_date = models.DateTimeField()
    description = models.TextField()
    image = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
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
