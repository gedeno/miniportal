from django.forms import ModelForm
from.models import studs, assessments, courses

class studt(ModelForm):
    class Meta:
        model = studs
        fields = ['name', 'id_no', 'age']
class formcourse(ModelForm):
    class Meta:
        model = courses
        fields = ['course_name']

class formgrade(ModelForm):
    class Meta:
        model = assessments
        fields = ['quiz1','quiz2','assignment','assignment2','mid_exam','final_exam']
       