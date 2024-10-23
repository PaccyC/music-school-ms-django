from django.urls import path
from . import views
urlpatterns=[
    path("/new",view=views.create_course),
    path("",view=views.get_all_courses),
    path("<int:pk>",view=views.get_course_by_id),
]