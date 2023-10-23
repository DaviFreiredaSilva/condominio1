from django.contrib import admin
from django.urls import path
from condominio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('galery', views.galery, name='galery'),
    path('residents', views.residents, name='residents'),
    path('visitors', views.visitors, name='visitors'),
]
