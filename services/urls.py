from django.urls import path
from services import views


urlpatterns = [
    path("", views.index, name="services"),
    path("web/", views.web, name="web"),
    path("software/", views.software, name="software"),
    path("training/", views.training, name="training"),
]
