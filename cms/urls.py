from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^index/$', views.index,name='index'),
    url(r'^cadastroProfessor/$', views.cadastroProfessor, name='cadastroProfessor')
]