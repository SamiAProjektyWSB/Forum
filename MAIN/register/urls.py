from django.urls import path, include
from .views import signup, signin, profile_update

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="sigin"),
    path("profile_update/", profile_update, name="profile_update"),
]