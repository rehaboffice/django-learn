from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    """
    Display a simple greeting on the home page.
    """
    return render(request, "home.html")