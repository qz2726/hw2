# from django.contrib import admin
# from django.urls import include, path
#
# urlpatterns = [
#     path("polls/", include("polls.urls")),
#     path("admin/", admin.site.urls),
# ]
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from django.shortcuts import render

# Simple view for the home page
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path("", home, name="home"),  # Add route for home page
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
