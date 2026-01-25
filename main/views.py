from django.shortcuts import render, redirect
from . models import studs, grade
from . forms import *

# Create your views here.
def home(request):
    form = studt()
    if request.method == 'POST':
        form = studt(request.POST)
        if form.is_valid():
            form.save()
            grade1 = grade(student=form)
            grade1.save()

    return render(request, 'home.html', {'form':form})
def teach(request):
    if request.method == "GET":
        id_no = request.GET.get('id_no')
        stud = studs.objects.get(id_no=id_no)
        if stud:
            return redirect(f"/teach/{stud.id}")
    return render(request, 'teach.html')
def teach2(request,id):
    stud = studs.objects.get(id=id)
    grd = grade.objects.get(student=stud)
    form = studG(instance=grd)
    if request.method == "POST":
        form = studG(request.POST, instance=grd)
        if form.is_valid():
            form.save()
    return render(request,'main/teachh.html',{'form':form})

stud1 = None
grd = None
def display(request):

    if request.method == 'GET':
        name =request.GET.get('name')
        id_no = request.GET.get('id_no')
        global stud1
        global grd
        stud1 = studs.objects.get(id_no=id_no)
        if stud1:
            grd = grade.objects.get(student=stud1)
            

    return render(request, 'display.html', {'studs': stud1, 'grades': grd})