from django.urls import path
from . import views
urlpatterns=[
    path("data/",views.get_enrollment_data,name="enrollment_data"),
    path("new/",view=views.create_course,name="add_course"),
    path("all_courses/",view=views.get_all_courses,name="course_list"),
    path("<int:pk>/",view=views.get_course_by_id,name="course_detail"),
    path("<int:pk>/edit",view=views.edit_course,name="edit_course"),
    path("<int:pk>/delete",view=views.delete_course, name="delete_course"),
    path("enroll/<int:course_id>/",views.enroll_student,name="enroll_student"),
    path("student/enrollments/",views.student_enrollments,name="student_enrollments"),
    path("<int:course_id>/enrollments/",views.course_enrollments,name="course_enrollments"),
    path("unenroll/<int:enrollment_id>/",views.unenroll_students,name="unenroll_student"),
    path('teacher-workload/', views.teacher_workload_chart, name='teacher_workload_chart'),
]