"""prosystem_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from prosystem.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^api/test', test),
    re_path('^api/get_fields', get_field),
    re_path('^api/get_properties', get_properties),
    re_path('^api/handle_infer', handle_infer),
    re_path('^api/get_objectsList', get_objectsList),
    re_path('^api/handle_delete', handle_delete),
    re_path('^api/get_filterList', get_filterList),
    re_path('^api/handle_update', handle_update),
    re_path('^api/get_classList', get_classList),
    re_path('^api/handle_update', handle_update),
    re_path('^api/handle_field', handle_field),
]
