from django.urls import path
from . import views

urlpatterns = [
    path('loginUser', views.loginUser, name="loginUser"),
    path('authLogin', views.authLogin, name="authLogin"),
    path('authLogout', views.authLogout, name="authLogout"),
    path('authError', views.authError, name="authError"),
]