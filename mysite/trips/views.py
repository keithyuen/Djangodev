# trips/views.py

from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponse

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': datetime.now(),
    })
	
from .models import Post

def home(request):
   post_list = Post.objects.all()
   return render(request,'home.html',{
      'post_list': post_list,
   })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})