from django.shortcuts import get_object_or_404, redirect, render
from courses.models import Course
from progress.models import Attendance, Grade, Performance
from user_auth.models import CustomUser
from .forms import AttendanceForm, GradeForm, PerformanceForm
from django.contrib import messages
# Create your views here.



# Creating attendance

def make_attendance(request,course_id):
    course= get_object_or_404(Course,id=course_id)
    students=CustomUser.objects.filter(role='student')
    
    if request.method == 'POST':
        for student in students:
            present=request.POST.get(f"present_{student.id}","off") == "on"
            Attendance.objects.create(
                student=student,
                course=course,
                date=request.POST['date'],
                present=present,
                
            )
        messages.success(request,"Attendance has been successfully recorded")  
        return redirect("course_attendance",course_id=course_id)
    
    context = {
        'course':course,
        "students":students
    }
    return render(request,"attendance/mark_attendence.html",context)


def view_attendance_by_student(request,student_id):
    student= get_object_or_404(CustomUser,id=student_id,role='student')
    attendances= Attendance.objects.filter(student=student)
    context={
        'student':student,
        'attendances':attendances
    }
    return render(request,'attendance/student_attendance.html')


def view_attendance_by_course(request,course_id):
    
    course= get_object_or_404(Course,id=course_id)
    attendances= Attendance.objects.filter(course=course)
    context= {
        'course':course,
        'attendances':attendances
    }
    return render(request,'attendance/course_attendance.html',context)


def view_grades_by_student(request, student_id):
    student = get_object_or_404(CustomUser, id=student_id, role='student')
    grades = Grade.objects.filter(student=student)
    context = {
        'student': student,
        'grades': grades
    }
    return render(request, 'grades/student_grades.html', context)


def add_grade(request,course_id):
    course=get_object_or_404(Course,id=course_id)
    students=CustomUser.objects.filter(role='student')
    
    if request.method == 'POST':
        for student in students:
            score=request.POST.get(f'score_{student.id}')
            feedback=request.POST.get(f'feedback_{student.id}', '')
            
            if score:
                Grade.objects.create(
                    student=student,
                    course=course,
                    score=score,
                    feedback=feedback
                )
        messages.success(request,'Grades have been added successfully')
        return redirect('course_grades',course_id=course_id)
    
    context ={
        'course':course,
        'students':students
    }         
    
    return render(request,'grades/add_grade.html',context)


def view_grades_by_course(request,course_id):
    course=get_object_or_404(Course,id=course_id)
    grades=Grade.objects.filter(course=course)
    
    context = {
        'course':course,
        'grades':grades
    }
    return render(request,'grades/course_grades.html',context)



def edit_grade(request,grade_id):
    grade= get_object_or_404(Grade,id=grade_id)
    if request.method == 'POST':
        form=GradeForm(data=request.POST,instance=grade)
        if form.is_valid():
            form.save()
            messages.success(request,"Grade has been updated successfully")
            return redirect('student_grades',student_id=grade.student.id)
        
    else:
        form=GradeForm(instance=grade)
    
    context={
        'form':form,
        'grade':grade
    }
    
    return render(request,'grades/edit_grade.html',context)



def record_performance(request,student_id):
    student=get_object_or_404(CustomUser,id=student_id,role='student')
    
    if request.method == 'POST':
        form=PerformanceForm(request.POST)
        if form.is_valid():
            performance=form.save(commit=False)
            performance.student=student
            performance.save()
            messages.success(request,"Performance has been recorded successfully")
            return redirect('student_performance',student_id=student_id)
        
    else:
        form=PerformanceForm()
        
    context ={
        'student':student,
        'form':form,
    }        
    return render(request,'performance/record_performance.html',context)



def view_performances_by_student(request,student_id):
    student=get_object_or_404(CustomUser,id=student_id,role='student')
    performances=Performance.objects.filter(student=student).order_by('-date')
    
    context = {
        'student':student,
        'performances':performances
    }
    return render(request,'performance/student_performances.html',context)