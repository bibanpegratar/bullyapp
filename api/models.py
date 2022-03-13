import unittest
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# create a new user
# create a superuser

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

