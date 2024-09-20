from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True,max_length=100)
    email = models.EmailField(unique=True, validators=[EmailValidator()])

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300)
    bio = models.CharField(max_length=300)
    image = models.ImageField(default="default.jpg",upload_to="user_images")
    verified = models.BooleanField(default=False)

    

    def __str__(self):
        return self.full_name


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)