# from django.shortcuts import render
# from .models import Post

# # Create your views here.
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'posts/post_list.html', {'posts': posts})

from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'posts/post_list.html'