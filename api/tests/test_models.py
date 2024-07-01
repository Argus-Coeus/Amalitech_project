from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Profile

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_profile_creation(self):
        profile = Profile.objects.get(user=self.user)
        self.assertTrue(isinstance(profile, Profile))
        self.assertEqual(profile.user.username, 'testuser')
