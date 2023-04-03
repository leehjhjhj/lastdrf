from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# ...
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
# ...

class BlogList(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
	authentication_classes = [BasicAuthentication, SessionAuthentication]
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
		
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)

...
from django.shortcuts import get_object_or_404
...


class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
	authentication_classes = [BasicAuthentication, SessionAuthentication]
    #authentication_classes = [JWTAuthentication]