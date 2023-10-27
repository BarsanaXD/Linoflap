from django.urls import path
from app.views import *
urlpatterns = [
    path('home', ReactView.as_view()),
]
