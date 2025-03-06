from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


urlpatterns = [
    path("", home, name="home"),  # Add route for home page
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
