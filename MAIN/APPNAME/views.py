from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})

def posts(request):
    return render(request, "posty.html", {})

def posts_detailed(request):
    return render(request, "post-szczegoly.html", {})