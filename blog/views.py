from .models import Blog, GuestBook
from .serializers import BlogSerializer, GuestBookSerializer


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# ...
from rest_framework.generics import ListCreateAPIView
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

class GuestBookListcreate(ListCreateAPIView):
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer

class GuestBookDetail(RetrieveUpdateDestroyAPIView):
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer
