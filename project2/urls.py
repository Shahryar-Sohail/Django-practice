

from django.urls import path , include
from . import views

urlpatterns = [
    path("", views.all_project2, name="all_project2"),
 
]
