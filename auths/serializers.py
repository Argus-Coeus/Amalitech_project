from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from package.django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from api.models import Profile
from django.contrib.auth import authenticate
from .utils import send_verification_email


User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD   

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claim to the token
        token['email'] = user.email
        return token

    def validate(self, attrs):
        email = attrs.get(self.username_field)
        password = attrs.get('password')
         # Check if both email and password are provided
        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")

        # Check if both email and password are provided
        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")

        try:
            # Check if the user with the provided email exists
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials.")

        # Authenticate user based on email and password
        user = authenticate(email=email, password=password)

        if not user.profile.is_verified:
            raise serializers.ValidationError("Account is not verified.")

        # Call parent's validate method to obtain tokens
        data = super().validate(attrs)
        refresh_token = data.get('refresh')

        # Check if refresh token is valid and not blacklisted
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.check_blacklist()
            except RefreshToken.DoesNotExist:
                raise serializers.ValidationError("Token is blacklisted or invalid.")

        return data

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        # Create the associated Profile if it doesn't exist
        Profile.objects.get_or_create(user=user)

        # Send verification email
        send_verification_email(user)
        
        return user

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    
    def validate(self, attrs):
        return attrs    