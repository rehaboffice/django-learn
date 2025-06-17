from django.shortcuts import render
from django.views.generic import TemplateView

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

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_info"] = "This is the about page of our Django application."
        context["team_members"] = ["Alice", "Bob", "Charlie"]
        return context