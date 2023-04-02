from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model() 
# Create your models here.
class Workshop(models.Model):
    id = models.UUIDField(primary_key=True,blank=True)
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
    mentors = models.ManyToManyField(  # ValueError: "<Workshop: Workshop object (None)>" needs to have a value for field "id" before this many-to-many relationship can be used.
        User,
        verbose_name='workshops',
        blank=True,
        default='there are currently no mentors',
    )
    mentor_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.mentor_count = self.mentors.count()
        super().save(*args, **kwargs)

    
#attempting workshop_mentor model to store list of users who have signed up
# class WorkshopMentors(models.Model):
#     mentor_applied = models.BooleanField()
#     created_at = models.DateTimeField(auto_now_add=True)
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
#     current_mentor_num = models.ManyToManyField(
#         User,
#         related_name='mentor_counter'
#     )
#     class Meta:
#         unique_together = ('workshops', 'mentor')