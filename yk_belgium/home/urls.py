from django.urls import path 
from .views import HomeView, send_form

app_name ="home"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('send-form/', send_form, name="send-form"),
]