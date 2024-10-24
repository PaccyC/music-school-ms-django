from django import forms

from courses.models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model= Course
        fields= "__all__"
          
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md'}),
            'description': forms.Textarea(attrs={'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md'}),
            'teacher': forms.Select(attrs={'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md'}),
            'start_date': forms.DateInput(attrs={'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md', 'type': 'date'}),
            'schedule': forms.Textarea(attrs={'class': 'mt-1 block w-full p-2 border border-gray-300 rounded-md'}),
        }