from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    return render(request, "index/index.html")
