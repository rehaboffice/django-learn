from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    """
    Display a simple greeting on the home page.
    """
    return HttpResponse("<h1>Hello, World!</h1>")