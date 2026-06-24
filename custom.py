from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
       
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user
              
    def create_superuser(self,email,password=None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()
        return user 
        

class User(AbstractBaseUser): 
        email = models.EmailField()
        phone = models.CharField(max_length=10)
        is_active = models.BooleanField(default=True)
        is_admin = models.BooleanField(default=False)
        objects = UserManager()
        USERNAME_FIELD = 'email'
        
