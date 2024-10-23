from django.urls import path
from . import views
urlpatterns=[
    path('attendance/mark/<int:course_id>/', views.make_attendance, name='mark_attendance'),
    path('attendance/student/<int:student_id>/', views.view_attendance_by_student, name='student_attendance'),
    path('attendance/course/<int:course_id>/', views.view_attendance_by_course, name='course_attendance'),

    # Grades
    path('grades/add/<int:course_id>/', views.add_grade, name='add_grade'),
    path('grades/student/<int:student_id>/', views.view_grades_by_student, name='student_grades'),
    path('grades/course/<int:course_id>/', views.view_grades_by_course, name='course_grades'),
    path('grades/edit/<int:grade_id>/', views.edit_grade, name='edit_grade'),

    # Performance
    path('performance/record/<int:student_id>/', views.record_performance, name='record_performance'),
    path('performance/student/<int:student_id>/', views.view_performances_by_student, name='student_performances'),
]