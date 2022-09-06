from django.shortcuts import render
from myfiles.models import *
# Create your views here.
def index(malumot):
    maxs=Maxsulotlar.objects.all()
    pro = Projects.objects.all()
    return render(malumot, 'index.html', {'maxs': maxs,'pro':pro})
def about(malumot):
    ish = Ishchilar.objects.all()
    return render(malumot,'about.html',{'ish':ish})
def blog(malumot):
    return render(malumot,'blog.html')
def contact(malumot):
    return render(malumot,'contact.html')
def main(malumot):
    return render(malumot,'main.html')
def project(malumot):
    ish = Projects.objects.all()
    return render(malumot,'project.html',{'ish':ish})
def services(malumot):
    maxs = Maxsulotlar.objects.all()
    return render(malumot,'services.html',{'maxs':maxs})
def single(malumot):
    return render(malumot,'single.html')