from django.urls import path
from .views import home, posts, posts_detailed

urlpatterns = [
    path("", home, name="home"),
    path("posty/", posts, name="posts"),
    path("szczegoly/", posts_detailed, name="posts_detailed"),
]