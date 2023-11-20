from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django.contrib.auth.models import User


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        user = self.create_user(email, first_name, last_name, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractUser):

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True) 
    REQUIRED_FIELDS = ['first_name', 'last_name']
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username