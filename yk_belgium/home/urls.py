from django.urls import path 
from .views import HomeView, contact_view

app_name ="home"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('send-form/', contact_view, name="send-form"),
]