from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    """
    Display a simple greeting on the home page.
    """

    context = {
        "inventory_list": ["Apples", "Bananas", "Cherries"],
        "greeting": "Welcome to the Home Page!",
        "description": "This is a simple Django application.",
    }
    return render(request, "home.html", context)