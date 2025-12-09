from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.all_project2, name="all_project2"),
    path("<int:id>/", views.project2_detail, name="project2_detail"),
    path("project_shop", views.project_shop, name="project_shop"),
]
