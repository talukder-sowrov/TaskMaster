from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name = 'search'),
    path('jobs_list/',views.jobs_list, name = 'jobs_list')
]