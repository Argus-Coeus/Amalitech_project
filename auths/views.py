from django.shortcuts import redirect, render
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth.tokens import default_token_generator
from api.models import Profile
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from .serializers import LogoutSerializer
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

class MyObtainTokenPairView(TokenObtainPairView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
class LogoutView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        refresh_token = serializer.validated_data['refresh_token']
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except InvalidToken:
            return Response({"detail": "Token is blacklisted or invalid"}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({"detail": "Token error occurred"}, status=status.HTTP_400_BAD_REQUEST)
        
        response = Response(status=status.HTTP_205_RESET_CONTENT)
        response.delete_cookie('access')
        response.delete_cookie('refresh')
        return response
    
    def get_serializer(self, *args, **kwargs): # Import your custom serializer for the logout endpoint
        return LogoutSerializer(*args, **kwargs)
        
class VerifyAccountView(APIView):
    # permission_classes = (AllowAny,)

    def get(self, request, uid, token):
        user = generics.get_object_or_404(User, id=uid)
        if default_token_generator.check_token(user, token):
            profile = Profile.objects.get(user=user)
            profile.is_verified = True
            profile.save()
            return Response({"message": "Account verified successfully."}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid verification link."}, status=status.HTTP_400_BAD_REQUEST)
    


class VerifyAccountView(APIView):
    # permission_classes = [AllowAny]

    def get(self, request, uid, token):
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.profile.is_verified = True
            user.profile.save()
            return render(request, 'done.html', {'videos': "hello"})
        else:
            return Response({'status': 'Verification link is invalid'}, status=400)