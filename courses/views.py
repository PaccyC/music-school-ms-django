from django.shortcuts import redirect, render

from courses.forms import CourseForm
from courses.models import Course

# Create your views here.

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('', pk=course.pk)
        else:
            return render(request, 'course/create_course.html', {'form': form})
    else:
        form = CourseForm()
        return render(request, 'course/create_course.html', {'form': form})

# Getting all courses

def get_all_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        return render(request, 'course/course_list.html', {'courses': courses})

# Getting a single course

def get_course_by_id(request,pk):
    if request.method == 'GET':
        course = Course.objects.get(pk=pk)
        return render(request, 'course/course_detail.html', {'course': course})
  
    
    #Deleting a course
    

def delete_course(request,pk):
    if request.method == "POST":
        course= Course.objects.get(pk=pk)
        course.delete()
        
        return redirect('course_list')     
    
    
def edit_course(request,pk):
    if request.method == "POST":
        course = Course.objects.get(pk=pk)
        form = CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=course.pk)
        else:
            return render(request, 'edit_course.html', {'form': form, 'course': course})
    else:
        form = CourseForm()
        return render(request, 'course/edit-course.html', {'form': form})
