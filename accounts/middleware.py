import re
from django.shortcuts import render
from django.http import HttpResponseForbidden

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.excluded_paths = [
            re.compile(r'^/auth/login/$'),
            re.compile(r'^/forgot-password/$'),
            re.compile(r'^/login/$'),
            re.compile(r'^/$'),
            re.compile(r'^/logout/$'),
            re.compile(r'^/auth/logout/$'),
            re.compile(r'^/api/v1/vd/\d+/$'),
            re.compile(r'^/api/v1/vd/.*$'),
            re.compile(r'^/signup/$'),
            re.compile(r'^/upload/$'),
            re.compile(r'/video/\d+/$'), 
            re.compile(r'^/media/uploads/\d+/$'),
            re.compile(r'^/home/$'),  
            re.compile(r'^/dashboard/$'),  
            re.compile(r'^/home/\d+/$'),
            re.compile(r'^/media/uploads/video_files/.*$'),
            re.compile(r'^/super/$'),
            re.compile(r'^/media/uploads/thumbnails/.*$'),
            re.compile(r'^/auth/register/.*$'),
            re.compile(r'^/admin/login/$'),
            re.compile(r'^/admin/.*$'),
            re.compile(r'^/signup/.*$'),
            re.compile(r'^/auth/check-verification-status/.*$'),
            re.compile(r'^/api/v1/.*$'),
            re.compile(r'^/api/v1/reset/confirm/.*$'),
            re.compile(r'^/auth/verify/.*$'),
            re.compile(r'^/api/password_reset/.*$'),
            re.compile(r'^/reset-password-confirm/.*$'),
            re.compile(r'^/api/v1/reset/confirm/$'),
            re.compile(r'^api/docs/$'),
            re.compile(r'^/static/.*$'),
            re.compile(r'^/opt/render/project/.*$'),
            re.compile(r'^/static/.*$'),

            
        ]

    def __call__(self, request):
        if self.should_exclude_path(request.path):
            return self.get_response(request)

        # Check for access and refresh tokens in headers or cookies
        access_token = request.headers.get('Access-Token')
        refresh_token = request.headers.get('Refresh-Token')

        if not access_token or not refresh_token:
            access_token = request.COOKIES.get('access_token')
            refresh_token = request.COOKIES.get('refresh_token')

        # If either token is missing, return a 403 Forbidden response
        if not access_token or not refresh_token:
            return HttpResponseForbidden(render(request, '403.html'))

        # Tokens are present, proceed with the request
        response = self.get_response(request)
        return response

    def should_exclude_path(self, path):
        for pattern in self.excluded_paths:
            if pattern.match(path):
                return True
        return False
