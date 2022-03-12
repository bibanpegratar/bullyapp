import unittest
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# create a new user
# create a superuser

class AccountManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("no email adress provided")
        user = self.model(
            email=self.normalize_email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user= self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

# Create your models here.
class User(AbstractBaseUser):

    username = models.CharField(max_length=26, default = 'fffff')
    password = models.CharField(max_length=90, null=False, blank=False)
    email = models.EmailField(verbose_name='email adress', max_length=100, unique=True, blank=False)
    created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, null=True, editable=False)
    validated = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(defaul=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Post(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    caption = models.CharField(max_length=250, default='')
    content = models.CharField(max_length=2500, default='')
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, null=True, editable=False)

class Comment(models.Model):
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE, db_column='post_id')
    content = models.CharField(max_length=500, default='')
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, null=True, editable=False)

