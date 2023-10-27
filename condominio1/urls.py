from django.contrib import admin
from django.urls import path
from condominio import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('residents', views.residents, name='residents'),
    path('visitors', views.visitors, name='visitors'),
    path('config', views.config, name='config'),
    path('avisoEdit', views.avisoEdit, name='avisoEdit'),
]

urlpatterns += staticfiles_urlpatterns()
