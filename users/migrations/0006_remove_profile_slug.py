# Generated by Django 2.2.4 on 2019-12-25 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]
