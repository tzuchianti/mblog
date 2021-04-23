from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Post
# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    context = {
        'posts':posts,
        'now':now,
    }
    return render(request, 'homepage.html', context=context)
    