from django.shortcuts import render
from . models import studs, grade

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id_no = request.POST.get('id_no')
        age = request.POST.get('age')

        stud1 = studs(name = name,
                      id_no= id_no,
                      age = age)
        stud1.save()
        quiz1 = 0
        quiz2 = 0
        assignment = 0  
        assignment2 = 0
        mid_exam = 0
        final_exam = 0
        grade1 = grade(quiz1=quiz1,
                       quiz2=quiz2,
                       assignment=assignment,
                       assignment2=assignment2,
                       mid_exam=mid_exam,
                       final_exam=final_exam,
                       student=stud1)
        grade1.save()
    return render(request, 'home.html')
def teach(request):
    stud1 = studs.objects.all()
    grade1 = grade.objects.all()
    return render(request, 'teach.html')



def display(request):
    if request.method == 'POST':
        name =request.POST.get('name')
        id_no = request.POST.get('id_no')
        if stud1.name == name and stud1.id_no == id_no:
            stud1 = studs.objects.all()
            grade1 = grade.objects.all()

    return render(request, 'display.html', {'studs': stud1, 'grades': grade1})