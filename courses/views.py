from django.shortcuts import redirect, render

from courses.forms import CourseForm
from courses.models import Course
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
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
@login_required
def get_all_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        # Call Paginator and give it the query_set and number of items per-page 
        paginator= Paginator(courses,5)
        # get page number
        page_number= request.GET.get('page',1)
        
        # Get the number of items per page
        courses_page=paginator.get_page(page_number)
        
        
        
        return render(request, 'course/course_list.html', {'courses': courses_page})

# Getting a single course
@login_required
def get_course_by_id(request,pk): 
    if request.method == 'GET':
        course = Course.objects.get(pk=pk)
        return render(request, 'course/course_detail.html', {'course': course})
  
    
    #Deleting a course
    
@login_required
def delete_course(request,pk):
    if request.method == "POST":
        course= Course.objects.get(pk=pk)
        course.delete()
        
        return redirect('course_list')     
    
@login_required    
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
