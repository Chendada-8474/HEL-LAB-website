from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('project.html', views.project, name="project"),
]