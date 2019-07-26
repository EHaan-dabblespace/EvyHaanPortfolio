from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog


# Create your views here.
class BlogListView(ListView):
    template_name = './blog_list.html'
    model = Blog

    def get_queryset(self):
        return Blog.objects.all()
    
    