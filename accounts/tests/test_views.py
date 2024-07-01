from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from rest_framework import status

class TestLoginView(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')

    def test_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    # @patch('requests.post')
    # def test_login_view_POST_success_admin(self, mock_post):
    #     mock_response = mock_post.return_value
    #     mock_response.status_code = status.HTTP_200_OK
    #     mock_response.json.return_value = {
    #         'access': 'dummy_access_token',
    #         'refresh': 'dummy_refresh_token'
    #     }

    #     response = self.client.post(self.login_url, {
    #         'username': 'arguscoeus',
    #         'password': 'admin_password'
    #     })

    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('admin_list'))
    #     self.assertIn('access', response.cookies)
    #     self.assertIn('refresh', response.cookies)
    #     self.assertIn('detail', response.cookies)

    # @patch('requests.post')
    # def test_login_view_POST_success_user(self, mock_post):
    #     mock_response = mock_post.return_value
    #     mock_response.status_code = status.HTTP_200_OK
    #     mock_response.json.return_value = {
    #         'access': 'dummy_access_token',
    #         'refresh': 'dummy_refresh_token'
    #     }

    #     response = self.client.post(self.login_url, {
    #         'username': 'user',
    #         'password': 'user_password'
    #     })

    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, reverse('video_list'))
    #     self.assertIn('access', response.cookies)
    #     self.assertIn('refresh', response.cookies)

    # @patch('requests.post')
    # def test_login_view_POST_failure(self, mock_post):
    #     mock_response = mock_post.return_value
    #     mock_response.status_code = status.HTTP_401_UNAUTHORIZED
    #     mock_response.json.return_value = {
    #         'error': 'Invalid credentials'
    #     }

    #     response = self.client.post(self.login_url, {
    #         'username': 'invalid_user',
    #         'password': 'invalid_password'
    #     })

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'registration/login.html')
    #     self.assertIn('error', response.context)
