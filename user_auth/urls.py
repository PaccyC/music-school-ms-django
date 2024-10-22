from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path("",view=views.create_user,name="create_user"),
    path("login/",view=TokenObtainPairView.as_view()),
    path("token/refresh/",view=TokenRefreshView.as_view()),
    path("all/",view=views.get_users,name="get_users"),
    path("<int:pk>/",view=views.update_user,name="update_user"),
    path("<int:pk>/delete",view=views.remove_user,name="remove_user"),
    
]