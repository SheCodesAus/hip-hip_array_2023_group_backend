# Generated by Django 4.0.2 on 2023-03-27 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(choices=[('python', 'Python'), ('django', 'Django'), ('react', 'React'), ('javascript', 'JavaScript'), ('htmlcss', 'HTML/CSS')], default=None, max_length=100, null=True)),
                ('title', models.CharField(max_length=200)),
                ('workshop_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('image', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_open', models.BooleanField()),
                ('current_mentor_num', models.IntegerField()),
                ('max_mentor_num', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshop_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
