from django.contrib import admin
from django.urls import path, include
from condominio import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('residents', views.residents, name='residents'),
    path('visitors', views.visitors, name='visitors'),
    path('config', views.config, name='config'),
    path('avisoManage', views.avisoManage, name='avisoManage'),
    path('avisoDetails/<int:id>', views.avisoDetails, name='avisoDetails'),
    path('avisoEdit/<int:id>', views.avisoEdit, name='avisoEdit'),
    path('avisoDelete/<int:id>', views.avisoDelete, name='avisoDelete'),
    path('accounts/', include('accounts.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
