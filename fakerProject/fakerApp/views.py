from django.shortcuts import render
from fakerApp.models import student

# Create your views here.
def view(request):
    s=student.objects.all()
    d={"student":s}
    return render(request,"fakerApp/1.html",d)
