from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=26, null=True, default=NULL)
    password = models.CharField(max_length=90, null=False, blank=False)
    email = models.CharField(max_length=100, unique=True, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)
    validated = models.BooleanField(default=False)

class Post(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    caption = models.CharField(max_length=250, null=False, blank=False)
    content = models.CharField(max_length=2500, blank=True)
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, null=True, editable=False)

class Comment(models.Model):
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE, db_column='post_id')
    content = models.CharField(max_length=500, default='')
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, null=True, editable=False)

