# Generated by Django 5.0.6 on 2024-06-26 09:48

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile_pics/blank_profile.jpeg', null='True', upload_to=users.models.user_directory_path),
        ),
    ]
