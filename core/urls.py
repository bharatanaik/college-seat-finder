from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('admissions.urls')),
    path('', include('django.contrib.auth.urls')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]