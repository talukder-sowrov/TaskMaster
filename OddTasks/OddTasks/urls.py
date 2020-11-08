"""OddTasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url, include

from pages.views import *

urlpatterns = [
    path('test/', include('UserDB.urls')),
    path('', home_view),
    path('customer/', customer_view, name = 'customer'),
    path('worker/', worker_view, name = 'worker'),
    path('job1/', job_1_view, name = 'job1'),
    path('job2/', job_2_view, name = 'job2'),
    path('job3/', job_3_view, name = 'job3'),
    path('job4/', job_4_view, name = 'job4'),
    path('job5/', job_5_view, name = 'job5'),
    path('job6/', job_6_view, name = 'job6'),
    path('admin/', admin.site.urls),
]
