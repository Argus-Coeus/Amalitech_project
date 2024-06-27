import base64
from venv import logger
from django.conf import settings
from django.shortcuts import render, redirect
import requests
from django.views import View
from django.http import HttpResponseBadRequest,HttpResponseRedirect
from rest_framework.reverse import reverse
from rest_framework import status
from django.contrib import messages
from django.http import Http404
import jwt


API_URL = f'{settings.FRONTEND_URL}/api/v1/vd/'  





class Homepage(View):
    def get(self, request):
        return render(request, 'homepage.html')


class LoginView(View): 

    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        api_url = f'{settings.FRONTEND_URL}/auth/login/' 
        # auth_credentials = base64.b64encode(b'admin:admin').decode('utf-8')
        # headers = {
        #     'Authorization': f'Basic {auth_credentials}'
        # }
        data = {
              'username': username,
              'password': password,
          }
        response = requests.post(api_url,data)
        if response.status_code == status.HTTP_200_OK or response.status_code == 201:
            # print(response.status_code)
            # print(response.json())
            users = response.json()
            if username == "arguscoeus":
                redirect_url = 'admin_list' 
                response = HttpResponseRedirect(reverse(redirect_url))
                response.set_cookie('detail', "True", httponly=True)
                response.set_cookie('access', users['access'], httponly=True)
                response.set_cookie('refresh', users['refresh'], httponly=True)
                return response
            else:
                redirect_url = 'video_list'
                response = HttpResponseRedirect(reverse(redirect_url))
                response.set_cookie('access', users['access'], httponly=True)
                response.set_cookie('refresh', users['refresh'], httponly=True)
                return response
        else:
            errors = response.json()
            for field, messages_list in errors.items():
                for message in messages_list:
                    messages.error(request, message)
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
        


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

        api_url = f'{settings.FRONTEND_URL}/auth/register/'
        data = {
            "username": username,
            "password": password,
            "password2": confirm_password,
            "email": email,
            "first_name": first_name,
            "last_name": last_name
        }

        response = requests.post(api_url,data)
        if response.status_code == status.HTTP_200_OK or response.status_code == 201 :
            messages.success(request, f'{username} account created successfully. Verify your {email} account before you can login.')
            return render(request, 'registration/login.html')
        else:
            errors = response.json()
            for field, messages_list in errors.items():
                for message in messages_list:
                    messages.error(request, message)
            return render(request, 'registration/signup.html')

class ForgotPassword(View):
    def get(self, request):
        return render(request, 'registration/password_reset_form.html')


    def post(self, request):
        email = request.POST.get('email')
        api_url = f'{settings.FRONTEND_URL}/api/password_reset/'
        data = {
            "email": email
        }
        response = requests.post(api_url,data)
        if response.status_code == status.HTTP_200_OK or response.status_code == 201 :     
            return render(request, 'registration/password_reset_done.html')
        
        
class ForgotPasswordConfirm(View):
    def get(self, request):
        return render(request, 'registration/password_reset_confirm.html')   
    
    def post(self, request):
        password = request.POST.get('password')
        token = request.GET.get('token')
        data = {
            "password": password,
            "token" : token
        }
        api_url = f'{settings.FRONTEND_URL}/api/v1/reset/confirm/'
        response = requests.post(api_url,data)
        if response.status_code == status.HTTP_200_OK or response.status_code == 201 :     
            return redirect('login')
        else:
            errors = response.json()
            for field, messages_list in errors.items():
                for message in messages_list:
                    messages.error(request, message)
            return render(request, 'registration/password_reset_confirm.html', {'error': 'Invalid credentials'})
        
        

class Upload(View):
    def get(self, request):
        return render(request, 'upload.html')
    
    def post(self, request):
        author = request.POST.get('author')
        title = request.POST.get('title')
        description = request.POST.get('description')
        video_file = request.FILES.get("video")
        thumbnail = request.FILES['thumbnail']
        date_posted = request.POST.get('date_posted')
        
        data = {
            "author": 1,
            "title": title,
            "description": description,
            "date_posted": date_posted,
        }

        files = {
            "Video_file": video_file,
            "thumbnail": thumbnail
        }
        try:
            
            api_url = f'{settings.FRONTEND_URL}/api/v1/create/'
            response = requests.post(api_url, data=data, files=files)
            if response.status_code in (200, 201):
                return redirect('admin_list')
            else:
                logger.error(f"Upload Error")
        finally:
            video_file.close()
            thumbnail.close()

        return redirect('upload')  # Fallback redirect in case of failure
                
                
        


def admin_list(request):
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        videos = response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching videos: {e}")
        videos = []
    return render(request, 'admin.html', {'videos': videos})


def user_list(request):
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        videos = response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching videos: {e}")
        videos = []
    return render(request, 'list.html', {'videos': videos})

def video_detail(request, video_id):
    try:
        auth_credentials = base64.b64encode(b'admin:admin').decode('utf-8')
    
        response = requests.get(f"{API_URL}{video_id}/")
        response.raise_for_status()
        video = response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching video details: {e}")
        raise Http404("Video not found")
    return render(request, 'detail.html', {'video': video})



def logout(request):
    api_url = f'{settings.FRONTEND_URL}/auth/logout/'

    token = request.COOKIES.get('refresh')
    if token:
        data = {'refresh_token': token}
        try:
            response = requests.post(api_url, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return HttpResponseBadRequest(f"Error logging out: {e}")
    response = HttpResponseRedirect(reverse('login'))
    response.delete_cookie('detail')
    response.delete_cookie('access')
    response.delete_cookie('refresh')
    return response 