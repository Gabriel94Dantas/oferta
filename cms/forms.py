
from django import forms
from .models import professor
from .models import tipo_professor

class ProfessorForm(forms.ModelForm):

    def carregarTipoProfessor(self):
        tipos = tipo_professor.objects.retornarTodos()
        return tipos

    def salvarProfessor(self, professorSalvar):
        professorSalvar.save()

    class Meta:
        model = professor
        fields = ('id_professor', 'nome', 'matricula', 'id_tipo_professor', 'ativo')