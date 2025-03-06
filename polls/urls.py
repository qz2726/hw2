# from django.urls import path
#
# from . import views
#
# app_name = "polls"
# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
#     path("<int:pk>/", views.DetailView.as_view(), name="detail"),
#     path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]



from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
            <head><title>Welcome</title></head>
            <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
                <h1>Welcome to my Django app!</h1>
                <p>Click the button below to visit the polls page:</p>
                <a href="/polls/">
                    <button style="padding: 10px 20px; font-size: 16px; background-color: #007bff; color: #fff; border: none; border-radius: 5px; cursor: pointer;">
                        Go to Polls
                    </button>
                </a>
            </body>
        </html>
    """)

urlpatterns = [
    path("", home),  # Root URL shows the welcome message and button
    path("polls/", include("polls.urls")),  # Polls app
    path("admin/", admin.site.urls),       # Admin site
]
