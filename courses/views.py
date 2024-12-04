from django.shortcuts import redirect, render,get_object_or_404

from courses.forms import CourseForm, EnrollmentForm
from courses.models import Course, Enrollment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
# Create your views here.



def get_enrollment_data(request):
    enrollment_data=(
        Course.objects.annotate(student_count= Count("teacher_id"))
        .values("name","student_count")
    )
    
    
    
    return HttpResponse(enrollment_data)

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('course_list')
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



@login_required
def enroll_student(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form= EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=course.pk)
        
        else:
            return render(request, 'enrollment/enroll_student.html', {'form': form, 'course': course})
    
    else:
        form = EnrollmentForm(initial={'course':course, 'student': request.user})
        return render(request, 'enrollment/enroll_student.html', {'form': form, 'course': course})
    



@login_required
def course_enrollments(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollments = Enrollment.objects.filter(course=course)
    return render(request, 'enrollment/course_enrollments.html', {'enrollments': enrollments, 'course': course})


@login_required
def student_enrollments(request):
    enrollments= Enrollment.objects.filter(student= request.user)
    return render(request, 'enrollment/student_enrollments.html', {'enrollments': enrollments})
    
    
# Unenrollments
@login_required
def unenroll_students(request, enrollment_id):
    enrollment= get_object_or_404(Enrollment,pk=enrollment_id)
    if request.method == "POST":
        enrollment.delete()
        return redirect('student_enrollments')
    else:
        return render(request, 'enrollment/unenroll_confirm.html', {'enrollment': enrollment})
    




