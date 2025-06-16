from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse("Homepage")

def about_page_view(request):
    # return render(request, "pages/about.html")
    context = {"name": "John Doe", "age": 30}
    return render(request, "pages/about.html", context)