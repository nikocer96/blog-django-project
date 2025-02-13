from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Post
from django.views.generic import DetailView, ListView
from .forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

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

class SinglePostView(View):
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "posts_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)
        
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        context = {
            "post": post,
            "posts_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id") # comments è il nome nel modello in commenti con related_name
        }
        return render(request, "blog/post-detail.html", context)

# def post_detail(request, slug):
#     search_post = get_object_or_404(Post, slug = slug)
    
#     return render(request, "blog/post-detail.html", {
#         "search_post": search_post,
#         "posts_tags": search_post.tags.all()
#     })

class ReadLaterView(View):
    
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        return render(request, "blog/stored-posts.html", context)
            
    
    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        
        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")
        