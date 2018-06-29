
from django import forms
from .models import professor
from .models import tipo_professor
from .models import disciplina
from .models import usuario
from .models import tipo_disciplina
from .models import cargo
from .models import rel_professor_disciplina
from .dtos import cargoProf
from .dtos import DisciplinaDTO
from .enums import PontosDisciplina
from .enums import TipoDisciplina




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

    def carregarTodosCargos(self):
        return cargo.objects.retornarTodosAlfabetico()

    def retornarCargoProf(self,idProfessor):
        return cargo.objects.retornarCargosProfessor(idProfessor)

    def carregarCargoDto(self,idProfessor):
        cargos = self.carregarTodosCargos()
        cargosProf = self.retornarCargoProf(idProfessor)

        print(str(cargosProf) + 'Cargo Professor')

        cargosDTO = []
        for cargo in cargos:
            cargoDTO = cargoProf()
            if (cargosProf != None and cargo in cargosProf):
                cargoDTO.idCargo = cargo.id_cargo
                cargoDTO.nome = cargo.nome
                cargoDTO.checked = True
            else:
                cargoDTO.idCargo = cargo.id_cargo
                cargoDTO.nome = cargo.nome
                cargoDTO.checked = False

            cargosDTO.append(cargoDTO)

        return cargosDTO

    def carregarTodasDisciplinas(self):
        return disciplina.objects.retornarTodasDisciplinasAlfabetico()

    def retornarDisciplinaProfessor(self,idProfessor):
        return disciplina.objects.retornarDisciplinasProfessor(idProfessor)

    def carregarDisciplinaDTO(self,idProfessor):
        disciplinas = self.carregarTodasDisciplinas()
        disciplinasProfessor = self.retornarDisciplinaProfessor(idProfessor)

        disciplinasDTO = []

        for disciplina in disciplinas:

            disciplinaDTO = DisciplinaDTO()

            if (disciplinasProfessor != None and disciplina in disciplinasProfessor):

                disciplinaDTO.idDisciplina = disciplina.id_disciplina
                disciplinaDTO.nome = disciplina.nome
                disciplinaDTO.checked = True

            else:

                disciplinaDTO.idDisciplina = disciplina.id_disciplina
                disciplinaDTO.nome = disciplina.nome
                disciplinaDTO.checked = False

            disciplinasDTO.append(disciplinaDTO)

        return disciplinasDTO

    def retornarCargoPorId(self, idCargo):
        return cargo.objects.retornarCargoPorId(idCargo)

    def retornarDisciplinaPorId(self,idDisciplina):
        return disciplina.objects.retornarDisciplinaPorId(idDisciplina)

    def retornarQuantidadePontos(self, relProfessorDisciplina):

        if relProfessorDisciplina.id_cargo != None:
            return relProfessorDisciplina.id_cargo.pontos

        else:

            print('PRINT ENUM')
            print(PontosDisciplina.PROJETO_GRADUACAO.value)

            if relProfessorDisciplina.id_disciplina.id_tipo_disciplina.id_tipo_disciplina == TipoDisciplina.GRADUACAO.value:
                if relProfessorDisciplina.turno == 'Diurno':
                    pontos = relProfessorDisciplina.id_disciplina.creditos * PontosDisciplina.DISCIPLINA_DIURNO.value
                else:
                    pontos = relProfessorDisciplina.id_disciplina.creditos * PontosDisciplina.DISCIPLINA_NOTURNO.value

                if int(relProfessorDisciplina.numero_alunos) < 6:
                    print('Passei para dividir')
                    print(pontos)
                    print (float(float(pontos) / 2))
                    return float(float(pontos) / 2)

                return pontos

            if relProfessorDisciplina.id_disciplina.id_tipo_disciplina.id_tipo_disciplina == TipoDisciplina.TRABALHO_GRADUACAO.value:
                pontos = PontosDisciplina.PROJETO_GRADUACAO.value * float(relProfessorDisciplina.numero_alunos)
                return pontos

            if relProfessorDisciplina.id_disciplina.id_tipo_disciplina.id_tipo_disciplina == TipoDisciplina.PROJETO_LICENCIATURA.value:
                pontos = PontosDisciplina.PROJETO_GRADUACAO.value * float(relProfessorDisciplina.numero_alunos)
                return pontos

            if relProfessorDisciplina.id_disciplina.id_tipo_disciplina.id_tipo_disciplina == TipoDisciplina.INICIACAO_CIENTIFICA.value:
                pontos = PontosDisciplina.PERIODICO_OUTROS.value * float(relProfessorDisciplina.numero_alunos)
                return pontos

            if relProfessorDisciplina.id_disciplina.id_tipo_disciplina.id_tipo_disciplina == TipoDisciplina.MESTREDO.value:
                pontos = PontosDisciplina.PROJETO_MESTRADO.value * float(relProfessorDisciplina.numero_alunos)
                return pontos

            if relProfessorDisciplina.id_disciplina.id_tipo_disciplina.id_tipo_disciplina == TipoDisciplina.DOUTORADO.value:
                pontos = PontosDisciplina.PROJETO_DOUTORADO.value * float(relProfessorDisciplina.numero_alunos)
                return pontos

            if relProfessorDisciplina.id_disciplina.id_tipo_disciplina.id_tipo_disciplina == TipoDisciplina.A1.value:
                pontos = PontosDisciplina.PERIODICO_A1.value *  float(relProfessorDisciplina.numero_alunos)
                return pontos

            if relProfessorDisciplina.id_disciplina.id_tipo_disciplina.id_tipo_disciplina == TipoDisciplina.A2.value:
                pontos = PontosDisciplina.PERIODICO_A2.value * float(relProfessorDisciplina.numero_alunos)
                return pontos

            if relProfessorDisciplina.id_disciplina.id_tipo_disciplina.id_tipo_disciplina == TipoDisciplina.B1.value:
                pontos = PontosDisciplina.PERIODICO_B1.value * float(relProfessorDisciplina.numero_alunos)
                return pontos

            if relProfessorDisciplina.id_disciplina.id_tipo_disciplina.id_tipo_disciplina == TipoDisciplina.B2.value:
                pontos = PontosDisciplina.PERIODICO_B2.value * float(relProfessorDisciplina.numero_alunos)
                return pontos

            if relProfessorDisciplina.id_disciplina.id_tipo_disciplina.id_tipo_disciplina == TipoDisciplina.B3_B5.value:
                pontos = PontosDisciplina.PERIODICO_OUTROS.value * float(relProfessorDisciplina.numero_alunos)
                return pontos

    def salvarRelProfessorDisciplina(self,relProfessorDisciplinas):

        for relProfessorDisciplina in relProfessorDisciplinas:
            relProfessorDisciplina.save()







