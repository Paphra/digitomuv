from django.urls import path
from home import views 

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("feedback/", views.feedback, name="feedback"),
]
