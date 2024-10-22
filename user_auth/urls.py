from django.urls import path
from . import views
urlpatterns=[
    path("",view=views.create_user,name="create_user"),
    path("all/",view=views.get_users,name="get_users"),
    path("<int:pk>/",view=views.update_user,name="update_user"),
]