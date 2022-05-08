from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('sos/', views.sos, name='sos'),
    path('test/', views.test, name='test'),
]