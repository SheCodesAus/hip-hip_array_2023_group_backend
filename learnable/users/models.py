from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.EmailField(unique=True, null=True)
    last_login = None
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    password = models.CharField(max_length=1000, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    skills_choices = (
        ("python", "Python"),
        ("django", "Django"),
        ("react", "React"),
        ("javascript", "JavaScript"),
        ("htmlcss", "HTML/CSS"),
    )

    skills = models.CharField(max_length=100,
                              choices=skills_choices,
                              default=None, blank=True, null=True)

    def __str__(self):
        return self.username
