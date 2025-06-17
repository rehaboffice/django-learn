from django.urls import path

from .views import PostList
# from .views import post_list

urlpatterns = [
path("", PostList.as_view(), namee="home"),
]
