from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^index/$', views.index,name='index'),
    url(r'^cadastro/$', views.cadastro,name='cadastro'),
    url(r'^cadastroProfessor/$', views.cadastroProfessor, name='cadastroProfessor'),
    url(r'^cadastroDisciplina/$', views.cadastroDisciplina, name='cadastroDisciplina'),
    url(r'^cadastroCargo/$', views.cadastroCargo, name='cadastroCargo'),
    url(r'^professorDisciplinaPasso1/$', views.professorDisciplinaPasso1, name='professorDisciplinaPasso1'),
    url(r'^professorDisciplinaPasso2/$', views.professorDisciplinaPasso2, name='professorDisciplinaPasso2')
]