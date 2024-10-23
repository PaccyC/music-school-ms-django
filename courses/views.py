from django.shortcuts import redirect, render

from courses.forms import CourseForm
from courses.models import Course

# Create your views here.


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('course_list', pk=course.pk)
        else:
            return render(request, 'create_course.html', {'form': form})
        
        
# Getting all courses

def get_all_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        return render(request, 'course_list.html', {'courses': courses})


def get_course_by_id(request,pk):
    if request.method == 'GET':
        course = Course.objects.get(pk=pk)
        return render(request, 'course_detail.html', {'course': course})
  
    