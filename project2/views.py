from django.shortcuts import render
from .models import ProjectDetail , ProjectShop
from django.shortcuts import get_object_or_404
from .forms import ProjectDetailForm
# Create your views here.
def all_project2(request):
    project_details = ProjectDetail.objects.all()
    return render(request, 'project2/all_project2.html',{'project_details':project_details})

def project2_detail(request, id):
    details = get_object_or_404(ProjectDetail,pk=id)
    return render(request, 'project2/project2_detail.html',{'details':details})

def project_shop(request):
    stores = None
    if request.method == 'POST':
        form = ProjectDetailForm(request.POST)
        if form.is_valid():
            project_Details= form.cleaned_data['project_Details']
            shop = ProjectShop.objects.filter(ProjectDetails=project_Details)
    else:
        form = ProjectDetailForm()
    
    return render(request, 'project2/projectShop.html', {'stores':stores, 'form':form})
