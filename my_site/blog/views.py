from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def starting_page(request):
    return HttpResponse("ciao")

def posts(request):
    pass

def post_detail(request):
    pass