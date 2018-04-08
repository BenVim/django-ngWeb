"""ngrok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import view
from ngrokApp import views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', view.index),
    url(r'index', view.index),
    url(r'time', view.current_datetime),
    url(r'download', view.client_download),
    url(r'about', view.about),
    url(r'register', views.register),
    url(r'login', views.login),
    url(r'doc', view.doc),
    url(r'qq', view.qq),
    url(r'forget', view.forget),
    url(r'member/dashborad', views.userCenter),

]
