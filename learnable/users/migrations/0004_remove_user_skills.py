# Generated by Django 4.0.2 on 2023-03-25 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='skills',
        ),
    ]
