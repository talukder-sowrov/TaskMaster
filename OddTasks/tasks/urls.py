from django.urls import path

from . import views

#when a page is requested, the system looks at urlpatters to find a matching path, and then runs the corresponding view
urlpatterns = [

    path('', views.index, name='index'),
    path('initialize/', views.initialize,name='initialize'),
    path('search/', views.search, name = 'search'),
    path('jobs_list/',views.jobs_list, name = 'jobs_list')
]