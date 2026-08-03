from django.urls import path

from diretorio.blog.views.post_view import PostView

urlspatterns = [
    path('', PostView.as_view(), name='home'),
]