from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post


class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


