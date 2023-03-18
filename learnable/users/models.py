from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    last_login = None
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField(('email address'), unique=True)
    password = models.CharField(max_length=1000)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    skills_choices = (
        ("PY", "Python"),
        ("DJ", "Django"),
        ("RE", "React"),
        ("JS", "JavaScript"),
        ("HT", "HTML/CSS"),
    )

    skills = models.CharField(max_length=100,
                             choices=skills_choices,
                             default=None)
    # class Skill(models.TextChoices):
    #     PY = "Python"
    #     DJ = "Django"
    #     RE = "React"
    #     JS = "JavaScript"
    #     HT = "HTML/CSS"

    def __str__(self):
        return self.user
