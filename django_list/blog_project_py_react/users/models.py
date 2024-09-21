from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    username = models.CharField(unique=True,max_length=100)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    verified = models.BooleanField(default=False)
    
     # Specify the field to use for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

     # Role can be used to differentiate between authors and regular users
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('subscriber', 'Subscriber'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='subscriber')


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'  # Specify the custom table name here