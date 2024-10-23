from django import forms

from progress.models import Attendance,Grade

class AttendanceForm(forms.Form):
    class Meta:
        model = Attendance
        fields = "__all__"
        


class GradeForm(forms.Form):
    class Meta:
        model=Grade        
        fields= "__all__"
        

class PerformanceForm(forms.Form):
    class Meta:
        model= Grade
        fields = "__all__"        