from rest_framework import serializers
from dataclasses import field
from .models import Blog, GuestBook

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'body']
        read_only_fields = ['user']


class GuestBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestBook
        fields = ['id', 'name', 'content']
        read_only_fields = ['id']