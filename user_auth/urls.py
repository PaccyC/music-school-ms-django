from django.urls import path
from . import views


urlpatterns=[
    path("register/",view=views.create_user,name="create_user"),
     path("login/",view=views.user_login,name="login"),
    path("all/",view=views.get_users,name="get_users"),
    path("<int:pk>/",view=views.update_user,name="update_user"),
    path("<int:pk>/delete",view=views.remove_user,name="remove_user"),
    
]