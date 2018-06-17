
from django import forms
from .models import professor
from .models import tipo_professor
from .models import disciplina
from .models import tipo_disciplina

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


class DisciplinaForm(forms.ModelForm):

    def carregarTiposDisciplina(self):
        tipos = tipo_disciplina.objects.retornarTodos()
        return tipos

    def retornarTipoPorId(self,idTipoDisciplina):
        return tipo_disciplina.objects.retornarPorId(idTipoDisciplina)

    def salvarDisciplina(self,disciplinaSalvar):
        print(str(disciplinaSalvar.id_disciplina) + disciplinaSalvar.nome + disciplinaSalvar.creditos)

        if disciplinaSalvar.id_disciplina == None:
            disciplinaSalvar.save()
        else:
            disciplina.objects.editarDisciplina(disciplinaSalvar.id_disciplina,disciplinaSalvar)

    def excluirDisciplina(self,idDisciplina):
        disciplina.objects.excluirDisciplina(idDisciplina)

    def retornarDisciplinaPorId(self,idDisciplina):
        return disciplina.objects.retornarDisciplinaPorId(idDisciplina)

    def carregarDisciplinasAlfabetico(self):
        return disciplina.objects.retornarTodasDisciplinasAlfabetico()

    class Meta:
        model = disciplina
        fields = ('id_disciplina', 'nome', 'creditos', 'id_tipo_disciplina', 'ativo')