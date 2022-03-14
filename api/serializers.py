from rest_framework import serializers
from .models import *

# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=26)
#     password = serializers.CharField(max_length=90)
#     email = serializers.CharField(max_length=100)
#     created = serializers.DateTimeField()
#     last_modified = models.DateTimeField()

#     def create(self, validated_data):
#         return User.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.password = validated_data.get('password', instance.password)
#         instance.email = validated_data.get('email', instance.email)
#         instance.created = validated_data.get('created', instance.created)
#         instance.last_modified = validated_data.get('last_modified', instance.modified)
#         instance.save()
#         return instance
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['password', 'email']
        # read_only_fields = ['id', 'username', 'created', 'last_modified', 'validated']


class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'email']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
