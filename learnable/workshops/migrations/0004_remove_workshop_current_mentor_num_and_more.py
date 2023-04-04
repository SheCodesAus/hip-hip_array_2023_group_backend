# Generated by Django 4.0.2 on 2023-04-03 07:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshops', '0003_remove_workshop_skills_workshop_is_django_mentor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='current_mentor_num',
        ),
        migrations.AddField(
            model_name='workshop',
            name='mentor_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workshop',
            name='mentors',
            field=models.ManyToManyField(blank=True, default='there are currently no mentors', to=settings.AUTH_USER_MODEL, verbose_name='workshops'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='id',
            field=models.UUIDField(blank=True, primary_key=True, serialize=False),
        ),
    ]
