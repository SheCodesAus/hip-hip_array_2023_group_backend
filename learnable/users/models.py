from django.db import models
from django.contrib.auth.models import AbstractUser


# class Skill(models.Model):
#     name = models.CharField(max_length=64, unique=True)

#     def __str__(self):
#         return self.name


class User(AbstractUser):
    username = models.EmailField(unique=True, null=True)
    last_login = None
    is_python_mentor = models.BooleanField(default=False)
    is_django_mentor = models.BooleanField(default=False)
    is_react_mentor = models.BooleanField(default=False)
    is_javascript_mentor = models.BooleanField(default=False)
    is_htmlcss_mentor = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # skills = models.ManyToManyField(
    #     Skill, related_name="users", default=None, blank=True
    # )

    def __str__(self):
        return self.username
