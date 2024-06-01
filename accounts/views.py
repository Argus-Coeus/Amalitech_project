from django.shortcuts import render, redirect
import requests
from django.views import View
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse,HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.urls import reverse_lazy
from rest_framework import status
from django.urls import reverse_lazy
from django.contrib import messages


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

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        api_url = f'http://127.0.0.1:8000/auth/register/'

        data = {
            "username": username,
            "password": password,
            "password2": confirm_password,
            "email": email,
            "first_name": first_name,
            "last_name": last_name
        }

        print(data)
        print(api_url)

        response = requests.post(api_url,data)
        print(response.json())
        print(response.status_code)
        if response.status_code == status.HTTP_200_OK or response.status_code == 201 :     
            return redirect('login')
        else:
            errors = response.json()
            for field, message in errors.items():
                for message in message:
                    messages.error(request,message)
            return redirect('register')



class ForgotPassword(View):
    def get(self, request):
        return render(request, 'registration/password_reset_form.html')


    def post(self, request):
        email = request.POST.get('email')
