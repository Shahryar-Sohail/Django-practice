from django.shortcuts import render
from .models import ProjectDetail
# Create your views here.
def all_project2(request):
    project_details = ProjectDetail.objects.all()
    return render(request, 'project2/all_project2.html',{'project_details':project_details})
