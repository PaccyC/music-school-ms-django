from django.shortcuts import redirect, render

from courses.models import Course
from django.db.models import Count


# Create your views here.


def landingpage(request):
    if not request.user.is_authenticated:
        return redirect('login')  
    return render(request, 'home/home.html')



def teacher_workload_chart(request):
    teacher_workload=(
    Course.objects.values("teacher__username")
    .annotate(course_count=Count("id"))
    .order_by("-course_count")
    )
    
    
    labels= [entry['teacher__username'] for entry in teacher_workload]
    data = [entry['course_count'] for entry in teacher_workload]
    
    context = {
        'labels': labels,
        'data': data,
    }
    
    return render(request, 'home/home.html', context)