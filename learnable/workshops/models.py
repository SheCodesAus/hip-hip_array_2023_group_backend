from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Workshop(models.Model):
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
    max_mentor_num = models.IntegerField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="workshop_owner",
    ) 
    mentors = models.ManyToManyField( 
        User,
        related_name='workshops',
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def mentor_count(self):
        return self.mentors.count 