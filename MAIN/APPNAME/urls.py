from django.urls import path, include
from .views import home, posts, detail

urlpatterns = [
    path("", home, name="home"),
    path("posty/<slug>/", posts, name="posts"),
    path("szczegoly/<slug>/", detail, name="detail"),
    path('tinymce/', include('tinymce.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
]