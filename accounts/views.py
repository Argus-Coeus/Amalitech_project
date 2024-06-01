from django.shortcuts import render, redirect
import requests
from django.views import View
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse,HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.urls import reverse_lazy
from rest_framework import status


class LoginView(View):
    # success_url = 

    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        api_url = f'http://127.0.0.1:8000/auth/login/'  
        data = {
              'username': username,
              'password': password,
          }
        response = requests.post(api_url,data)
        if response.status_code == status.HTTP_200_OK:
            users = response.json()
#           print()
            response = JsonResponse({'access': str(users['access']), 'refresh': str(users['refresh'])})
            response.set_cookie('access', str(users['access']), httponly=True)
            response.set_cookie('refresh', str(users['refresh']), httponly=True)
            

            return render(request, 'space.html', {'message': 'Hello'})
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        response = redirect('login')
        response.delete_cookie('access')
        response.delete_cookie('refresh')
        return response


class SignView(View):
    
    def get(self, request):
        return render(request, 'registration/signup.html')



































