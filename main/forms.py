from django.forms import ModelForm
from.models import studs, grade

class studt(ModelForm):
    class Meta:
        model = studs
        fields = ['name', 'id_no', 'age']
class studG(ModelForm):
    class Meta:
        model = grade
        fields = ['quiz1','quiz2','assignment','assignment2','mid_exam','final_exam']
       