from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(unique=True, null=True)
    email = models.CharField
    is_python_mentor = models.BooleanField(default=False)
    is_django_mentor = models.BooleanField(default=False)
    is_react_mentor = models.BooleanField(default=False)
    is_javascript_mentor = models.BooleanField(default=False)
    is_htmlcss_mentor = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    # @property
    # def email(self):
    #     return self.username


# class UsersMentor(models.Model):
#         users_mentor = models.ManyToManyField('workshop_mentor')
