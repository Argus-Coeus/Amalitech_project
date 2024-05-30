from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
import requests

# # Create your views here.
def users(request):
    #pull data from third party rest api
    api_url = f'http://127.0.0.1:8000/auth/login/'  
    data = {
             'username': 'admin',
             'password': 'admin',
         }
    response = requests.post(api_url,data)
    if response.status_code == status.HTTP_200_OK:
        users = response.json()
        print(users['access'])
        requests.session['sessionid'] = users['access']
        print(requests.session)
    elif response.status_code    in [status.HTTP_400_BAD_REQUEST, status.HTTP_500_INTERNAL_SERVER_ERROR]:
        print(users)
        
    #convert reponse data into json
    # users = response.json()
    return HttpResponse("Users")

# def login(request):

#     if request.method == 'POST':
#         username = 'admin'
#         password = 'admin'

#         api_url = f'http://127.0.0.1:8000/auth/login/'  
#         data = {
#             'username': username,
#             'password': password,
#         }

#         try:

#             response = request.post(api_url, data=data)

#             if response['status'] == status.HTTP_200_OK:
#                 access_token = response.get('access')
#                 request.session['access'] = access_token
#                 return redirect('')
#             elif response['status'] in [status.HTTP_400_BAD_REQUEST, status.HTTP_500_INTERNAL_SERVER_ERROR]:
#                 messages.error(request, response['message'], extra_tags='error')   

#         except requests.exceptions.RequestException:
#             messages.error(request, 'Erro ao fazer login', extra_tags='error')

#     return render(request, r'')

# def login_dashboard(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username = username, password = password)
#         if user is not None and user.is_staff == False :
#             auth.login(request,user)
#             messages.success(request, f'You are Logged in {user}')
#             return redirect('myspace')
#         elif user is not None and user.is_staff == True and username == "admin":
#             auth.login(request,user)
#             messages.success(request, f'You are Logged in {user}')
#             return redirect('myspace')
        
#         else:
#             messages.error(request,'Your Username or Password is incorrect')
#             return redirect('accounts/login.html')
#         return
#     else:
#         return render(request,'accounts/login.html')
