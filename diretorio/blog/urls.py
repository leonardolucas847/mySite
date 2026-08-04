from django.urls import path

from diretorio.blog import views
from diretorio.blog.views.post_view import PostView

urlspatterns = [
    path('', views.PostView.as_view(), name='home'),
]