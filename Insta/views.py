from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# from django.contrib.auth.forms import UserCreationForm

from Insta.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AbstractUser


from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


from Insta.models import Post

# class HelloDjango(TemplateView):
#     template_name = '.html'

# Create your views here.

class PostsView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView, LoginRequiredMixin):  # createview pass 
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
    login_url = 'login'

class PostUpdateView(UpdateView):
    model = Post 
    template_name = 'post_update.html'
    fields = ['title'] # update title, not the picture

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')



