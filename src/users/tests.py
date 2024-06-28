from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileCreationTestCase(TestCase):
    def test_profile_created_on_user_creation(self):
        user = User.objects.create_user(username='testuser', password='password123')
        self.assertTrue(Profile.objects.filter(user=user).exists())

    def test_profile_creation_signal(self):
        user = User.objects.create_user(username='testuser2', password='password123')
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.user.username, 'testuser2')
