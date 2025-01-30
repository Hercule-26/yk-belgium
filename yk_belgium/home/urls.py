from django.urls import path 

app_name ="appartements"

urlpatterns = [
    path('be-fr/', "", name="home-fr"),
    path('send-form/', "", name="send-form"),
    path('be-nl/', "", name='home-nl'),
]