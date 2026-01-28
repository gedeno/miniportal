from django.db import models

# Create your models here.

class studs(models.Model):
    name = models.CharField(max_length=100)
    id_no = models.CharField(max_length=20,unique=True)
    age = models.IntegerField()
    def __str__(self):
        return self.name
    

class courses(models.Model):
    course_name = models.CharField(max_length=100)
    student = models.ForeignKey(studs, on_delete=models.CASCADE)
    def __str__(self):
        return self.course_name



class assessments(models.Model):
    quiz1 = models.FloatField(default=0)
    quiz2 = models.FloatField(default=0)
    assignment = models.FloatField(default=0)
    assignment2 = models.FloatField(default=0)
    mid_exam = models.FloatField(default=0)
    final_exam = models.FloatField(default=0)
    course = models.ForeignKey(courses, on_delete=models.CASCADE)
    def __str__(self):  
        return f"Grades of {self.student.name}"