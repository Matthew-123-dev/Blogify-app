from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .uploads import user_directory_path
from PIL import Image
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    num = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{num}"
        num += 1
    return unique_slug

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user.id}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null='True', upload_to= user_directory_path, default= 'profile_pics/blank_profile.jpeg')
    bio = models.TextField(blank=True, default='')
    phone_number = PhoneNumberField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}\'s profile'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.user.username))
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def generate_slug(self):
        slug = slugify(self.user.username)
        unique_slug = slug
        num = 1
        while Profile.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'slug': self.slug})


