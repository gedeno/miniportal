from django.shortcuts import render, redirect
from . models import studs, assessments,courses
from . forms import *

# Create your views here.
def home(request):
    form = studt()
    subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'English']
    if request.method == 'POST':
        form = studt(request.POST)
        if form.is_valid():
            st = form.save(commit=False)
            st.save()
            print(st.name)
            for sub in subjects:
                course1 = courses(course_name = sub, student=st)
                assessment = assessments(course = course1,student=st) 
                course1.save()
                assessment.save()

            return redirect("/home")
    return render(request, 'main/home.html', {'form':form})

def teach(request):
    if request.method == "POST":
        try:
            id_no = request.POST.get('id_no')
            stud = studs.objects.get(id_no=id_no)
            if stud:
                return redirect(f"/subject/{stud.id}")
        except studs.DoesNotExist:
            print("Student not found")
    return render(request, 'main/teach.html')

def Subject(request , id):
    stud = studs.objects.get(id=id)
    if request.method == "POST":
        course_id = request.POST.get('course')
        couerse = courses.objects.get(course_name=course_id, student=stud)
        return redirect(f"/teach2/{couerse.id}/")
    return render(request, 'main/subjects.html', {})

def teach2(request,id):
    course = courses.objects.get(id=id)
    grd = assessments.objects.get(course=course)
    form = formgrade(instance=grd)
    if request.method == "POST":
        form = formgrade(request.POST, instance=grd)
        if form.is_valid():
            form.save()
    return render(request,'main/teachh.html',{'form':form})


#display  student grades by id_no the templates are display and others 

def display(request):
    if request.method == 'POST':
        name =request.POST.get('name')
        id_no = request.POST.get('id_no')
        stud1 = studs.objects.get(id_no=id_no)
        if stud1:
            return redirect(f'/subjects1/{stud1.id}/')
    return render(request, 'main/display.html', {})

def subjects1(request, id):
    stud1 = studs.objects.get(id=id)
    if request.method == 'POST':
        course_id = request.POST.get('course')
        couerse = courses.objects.get(course_name=course_id, student=stud1)
        return redirect(f"/display2/{couerse.id}/")
    return render(request, 'main/subjects1.html', {})

def display2(request, id):
    std = studs.objects.get(id=id)
    course = courses.objects.get(id=id)
    grd = assessments.objects.get(course=course)
    sum_total = (grd.quiz1 + grd.quiz2 + grd.assignment + grd.assignment2 + grd.mid_exam + grd.final_exam)
    if sum_total >= 90:
        sum_total = f"{sum_total} : A+"
    if sum_total >= 85:
        sum_total = f"{sum_total} : A"
    elif sum_total >= 80:
        sum_total = f"{sum_total} : A-"
    elif sum_total >= 75:
        sum_total = f"{sum_total} : B+"
    elif sum_total >= 70:
        sum_total = f"{sum_total} : B"
    elif sum_total >= 65:
        sum_total = f"{sum_total} : B-"
    elif sum_total >= 60:
        sum_total = f"{sum_total} : C+"
    elif sum_total >= 50:
        sum_total = f"{sum_total} : C"
    elif sum_total >= 45:
        sum_total = f"{sum_total} : C-"
    elif sum_total >= 40:
        sum_total = f"{sum_total} : D"
    else:
        sum_total = f"{sum_total} : F"
    return render(request, 'main/display2.html', {'grd': grd, 'stud1': course, 'sum_total': sum_total,'std':std})
