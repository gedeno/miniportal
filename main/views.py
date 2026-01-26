from django.shortcuts import render, redirect
from . models import studs, grade
from . forms import *

# Create your views here.
def home(request):
    form = studt()
    if request.method == 'POST':
        form = studt(request.POST)
        if form.is_valid():
            st = form.save(commit=False)
            grade1 = grade(student=st)
            st.save()
            grade1.save()
        return redirect("/home")
    return render(request, 'main/home.html', {'form':form})
def teach(request):
    if request.method == "POST":
        try:
            id_no = request.POST.get('id_no')
            stud = studs.objects.get(id_no=id_no)
            if stud:
                return redirect(f"/teach2/{stud.id}")
        except studs.DoesNotExist:
            print("Student not found")
    return render(request, 'main/teach.html')


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
    
    if request.method == 'POST':
        name =request.POST.get('name')
        id_no = request.POST.get('id_no')
        global stud1
        global grd
        stud1 = studs.objects.get(id_no=id_no)
        
        grd = grade.objects.get(student=stud1)
            

    return render(request, 'main/display.html', {'studs': stud1, 'grades': grd})