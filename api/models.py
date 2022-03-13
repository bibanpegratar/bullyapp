import unittest
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, PermissionsMixin
from django.utils import timezone

# create a new user
# create a superuser

class UserManager(BaseUserManager):
    
  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')

    now = timezone.now()
    email = self.normalize_email(email)

    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        last_modified=now,
        **extra_fields
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user

# Create your models here

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return self.username

# class Post(models.Model):
#     user_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
#     caption = models.CharField(max_length=250, default='')
#     content = models.CharField(max_length=2500, default='')
#     likes = models.IntegerField(default=0)
#     created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
#     last_modified = models.DateTimeField(auto_now=True, null=True, editable=False)

# class Comment(models.Model):
#     post_id = models.ForeignKey('Post', on_delete=models.CASCADE, db_column='post_id')
#     content = models.CharField(max_length=500, default='')
#     likes = models.IntegerField(default=0)
#     created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
#     last_modified = models.DateTimeField(auto_now=True, null=True, editable=False)

