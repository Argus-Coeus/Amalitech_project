from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.urls import reverse

def send_verification_email(user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_link = f"{settings.FRONTEND_URL}{reverse('verify-account', kwargs={'uid': uid, 'token': token})}"

    subject = 'Verify your account'
    message = render_to_string('verification_email.txt', {
        'user': user,
        'verification_link': verification_link
    })

    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])