# Generated by Django 5.0.6 on 2024-06-22 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.DeleteModel(
            name='location',
        ),
    ]
