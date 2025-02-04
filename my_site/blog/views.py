from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Post

all_posts = [
    
]

# Create your views here.

def starting_page(request):
    list_posts = Post.objects.all().order_by("-date")
    
    return render(request, "blog/index.html", {
        "list_posts": list_posts
    })

def posts(request):
    all_posts = Post.objects.all()
    return render(request, "blog/all-posts.html", {
       "list_posts": all_posts 
    })

def post_detail(request, slug):
    search_post = get_object_or_404(Post, slug = slug)
    
    return render(request, "blog/post-detail.html", {
        "search_post": search_post,
        "posts_tags": search_post.tags.all()
    })