from django.urls import path
from . import views
urlpatterns=[
    path("new/",view=views.create_course,name="add_course"),
    path("all_courses/",view=views.get_all_courses,name="course_list"),
    path("<int:pk>/",view=views.get_course_by_id,name="course_detail"),
    path("<int:pk>/edit",view=views.edit_course,name="edit_course"),
    path("<int:pk>/delete",view=views.delete_course, name="delete_course"),
]