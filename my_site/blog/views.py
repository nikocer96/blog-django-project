from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Post
from django.views.generic import DetailView, ListView

all_posts = [
    
]

# Create your views here.

class StartingPage(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "list_posts"
    ordering = ["-title"]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:2]
        return data

# def starting_page(request):
#     list_posts = Post.objects.all().order_by("-date")
    
#     return render(request, "blog/index.html", {
#         "list_posts": list_posts
#     })

class Posts(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "list_posts"

# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/all-posts.html", {
#        "list_posts": all_posts 
#     })

class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "search_post"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["posts_tags"] = self.object.tags.all()
        return context

# def post_detail(request, slug):
#     search_post = get_object_or_404(Post, slug = slug)
    
#     return render(request, "blog/post-detail.html", {
#         "search_post": search_post,
#         "posts_tags": search_post.tags.all()
#     })