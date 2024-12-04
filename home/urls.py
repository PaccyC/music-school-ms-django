
from django.urls import path
from . import views

urlpatterns=[
    path("",views.teacher_workload_chart,name="home"),
]