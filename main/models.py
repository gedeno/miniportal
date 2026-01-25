from django.db import models

# Create your models here.

class studs(models.model):
    name = models.CharField(max_length=100)
    id_no = models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self):
        return self.name
class grade(models.Model):
    quiz1 = models.FloatField()
    quiz2 = models.FloatField()
    assignment = models.FloatField()
    assignment2 = models.FloatField()
    mid_exam = models.FloatField()
    final_exam = models.FloatField()
    student = models.ForeignKey(studs, on_delete=models.CASCADE)
    def __str__(self):  
        return f"Grades of {self.student.name}"