
from django import forms
from .models import professor
from .models import tipo_professor

class ProfessorForm(forms.ModelForm):

    def carregarTipoProfessor(self):
        tipos = tipo_professor.objects.retornarTodos()
        return tipos

    def salvarProfessor(self, professorSalvar):
        print(str(professorSalvar.id_professor) + professorSalvar.nome + professorSalvar.matricula)
        if professorSalvar.id_professor == None:
            professorSalvar.save()
        else:
            professor.objects.editarProfessores(professorSalvar.id_professor,professorSalvar)

    def carregarProfessoresAlfabetico(self):
        return professor.objects.retornarTodosProfessoresAlfabetico()

    def excluirProfessor(self,professorExcluir):
        professor.objects.excluirProfessor(professorExcluir.id_professor)

    def retornarProfessorPorId(self,idProfessor):
        return professor.objects.retornarPorId(idProfessor)

    class Meta:
        model = professor
        fields = ('id_professor', 'nome', 'matricula', 'id_tipo_professor', 'ativo')