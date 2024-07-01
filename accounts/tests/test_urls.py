from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import (
     Homepage, LoginView
)

class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_homepage_url_is_resolved(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func.view_class, Homepage)