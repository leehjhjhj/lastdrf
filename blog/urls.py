from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('guestbook/', GuestBookListcreate.as_view()),
    path('guestbook/<int:pk>/', GuestBookDetail.as_view()),

]