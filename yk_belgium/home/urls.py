from django.urls import path 
from .views import HomeViewFR, HomeViewNL, contact_view

app_name ="home"

urlpatterns = [
    path('be-fr/', HomeViewFR.as_view(), name="home-fr"),
    path('be-nl/', HomeViewNL.as_view(), name='home-nl'),
    path('send-form/', contact_view, name="send-form"),
]