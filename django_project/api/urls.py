from django.urls import path

from .views import update_post

urlpatterns = [
    path('post/<int:id>', update_post),
]
