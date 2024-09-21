from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db.models.signals import post_save
import random
import string
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    # by default providede list
    # username = models.CharField(unique=True,max_length=100)
    # email = models.EmailField(unique=True, validators=[EmailValidator()])
    # password
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_expiration = models.DateTimeField(null=True, blank=True)

     # Specify the field to use for authentication
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','role']

     # Role can be used to differentiate between authors and regular users
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('superadmin', 'Super Admin'),
        ('user', 'User'),
        ('moderator', 'Moderator'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='subscriber')
    plan_id = models.IntegerField(null=True, blank=True)


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'  # Specify the custom table name here

    def __str__(self):
        return self.username

    def generate_otp(self):
        self.otp = ''.join(random.choices(string.digits, k=6))
        self.otp_expiration = timezone.now() + timedelta(minutes=10)
        self.save()


    def send_otp_email(self):
        subject = 'Your OTP for Email Verification'
        message = f'Your OTP is {self.otp}. It is valid for 10 minutes.'
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [self.email],
            fail_silently=False,
        )