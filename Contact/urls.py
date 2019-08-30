from django.urls import path

from . import views

urlpatterns = [
    path('msg', views.msg, name='msg'),
]