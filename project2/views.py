from django.shortcuts import render
from .models import ProjectDetail
from django.shortcuts import get_object_or_404
# Create your views here.
def all_project2(request):
    project_details = ProjectDetail.objects.all()
    return render(request, 'project2/all_project2.html',{'project_details':project_details})

def project2_detail(request, id):
    details = get_object_or_404(ProjectDetail,pk=id)
    return render(request, 'project2/project2_detail.html',{'details':details})
