from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.

#The user will get its unique username only after validated = True
#Validated is set to true when the user confirms his email adress via link

#list of all users
#GET - return all users
#POST - insert user
class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get a user
#GET - return a user by pk
#PUT - update a user by pk
#DELETE - delete a user by pk
class UserDetailAPIView(APIView):
    
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#list of all posts
#GET - get all posts
#POST - insert post
class PostsAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#list of all posts of a user
#GET - get all posts of user with id=fk
class UserPostsAPIView(APIView):

    def get(self, request, fk):
        posts = Post.objects.filter(user_id=fk)
        serializer = PostSerializer(posts)
        return Response(serializer.data)

#a single post of a user
#GET - get a post of a user
#PUT - update a post
#DELETE - delete a post
class PostDetailAPIView(APIView):

    def get_post(self, fk, pk):
        try:
            return Post.objects.get(pk=pk, user_id=fk)
        except Post.DoesNotExist:
            return Response(status=404)

    def get(self, request, fk, pk):
        post = self.get_post(fk, pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, fk, pk):
        post = self.get_post(fk, pk)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requeset, fk, pk):
        post = self.get_post(fk, pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#list of all comments
#GET - get all comments
#POST - post a comment
class CommentsAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serialzier = CommentSerializer(comments)
        return Response(serialzier.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#comments of a post
#GET - get all comments of a post
class PostCommentAPIView(APIView):
    def get_post(self, fk):
        try:
            return Comment.objects.filter(post_id=fk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, fk):
        posts = self.get_post(fk)
        serializer = CommentSerializer(posts)
        return Response(serializer.data)


#TODO: Rewrite how a single comment is handled
#comments by id
#GET - get a comment by id
#PUT - update a comment
#DELETE - delete a comment
class CommentDetailAPIView(APIView):
    def get_comment(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        comment = self.get_comment(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def put(self, request, pk):
        comment = self.get_comment(pk)
        serializer = CommentSerializer(comment, request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_comment(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)