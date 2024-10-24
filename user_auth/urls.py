from django.urls import path
from . import views


urlpatterns=[
    path("register/",view=views.create_user,name="register"),
     path("login/",view=views.user_login,name="login"),
     path("logout/",view=views.user_logout,name="logout"),
    path("user_list/",view=views.user_list,name="user_list"),
      path("student_list/",view=views.student_list,name="student_list"),
    path("<int:pk>/",view=views.update_user,name="update_user"),
    path("<int:pk>/delete",view=views.remove_user,name="remove_user"),
    
]