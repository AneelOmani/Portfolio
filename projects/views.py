from django.shortcuts import render

from .models import Project, client
# Create your views here.

def project(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        des=request.POST['subject']
        c1=Project(name=fname,description=des)
        c1.save()
        pro=Project.objects.all()
        return render(request,'project.html',{'project':pro})
    else:
        pro=Project.objects.all()
        return render(request,'project.html',{'project':pro})