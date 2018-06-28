
from django import forms
from .models import professor
from .models import tipo_professor
from .models import disciplina
from .models import usuario
from .models import tipo_disciplina
from .models import cargo
from .models import rel_professor_disciplina





class LoginForm(forms.ModelForm):
    def autenticar(self, email, senha):
        return usuario.objects.autenticacao(email, senha)

    class Meta:
        model = usuario
        fields = ('id_usuario', 'email', 'nome', 'senha', 'ativo')

class CadastroForm(forms.ModelForm):
    def salvarUsuario(self, usuario):
        if usuario.id_usuario == None:
            usuario.save()



    class Meta:
        model = usuario
        fields = ('id_usuario', 'email', 'nome', 'senha', 'ativo')
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

class CargoForm(forms.ModelForm):

    def carregarCargosAlfabetico(self):
        return cargo.objects.retornarTodosAlfabetico()

    def retornarCargoPorId(self, idCargo):
        return cargo.objects.retornarCargoPorId(idCargo)

    def editar(self,cargoEditar):
        return cargo.objects.editarCargo(cargoEditar.id_cargo, cargoEditar)

    def excluir(self, idCargo):
        return cargo.objects.excluirCargo(idCargo)

    def salvar(self,cargoSalvar):
        if cargoSalvar.id_cargo == None:
            cargoSalvar.save()
        else:
            self.editar(cargoSalvar)

    class Meta:
        model = cargo
        fields = ('id_cargo', 'nome', 'ativo','pontos')

class RankingForm(forms.ModelForm):

    def carregarRankingPontuacaoDesc(self):
        return professor.objects.carregarRankingOrdenadoPontosDesc()

    def carregarRankingPontuacaoAsc(self):
        return professor.objects.carregarRankingOrdenadoPontosAsc()

    def carregarRankingAlfabetico(self):
        return professor.objects.carregarRankingOrdenadoNome()

    class Meta:
        model = professor
        fields = ('id_professor', 'nome', 'matricula')

class InfoProfForm(forms.Form):

    def retornarProfId(self,idprofessor):
        return professor.objects.retornarPorId(idprofessor)

    def carregartodoscargos(self):
        return cargo.objects.retornarTodosAlfabetico()

    def retornarCargoProf(self,idprofessor):
