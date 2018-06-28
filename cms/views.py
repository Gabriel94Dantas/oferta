from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ProfessorForm
from .models import tipo_professor
from .models import professor
from .forms import DisciplinaForm
from .models import disciplina
from .forms import LoginForm
from .models import usuario
from .forms import CadastroForm
from .forms import CargoForm
from .models import cargo
from .forms import RankingForm


# Create your views here.
def cadastro(request):
    context = {}
    template_name = 'oferta/cadastro.html'
    form = CadastroForm()
    if request.method == 'POST':
        form = CadastroForm()
        email = request.POST.get('emailC')
        senha = request.POST.get('senhaC')
        nome = request.POST.get('nomeC')
        Csenha = request.POST.get('Csenha')

        usuarioSalvar = usuario()

        usuarioSalvar.ativo = True
        usuarioSalvar.email = email
        usuarioSalvar.senha = senha
        usuarioSalvar.nome = nome
        form.salvarUsuario(usuarioSalvar)
        return redirect('/')
    return render(request, template_name, context)


def login(request):
    context = {}
    template_name = 'oferta/login.html'
    if request.method == 'POST':
        form = LoginForm()
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        print((form.autenticar(email, senha)))
        print(form.autenticar(email, senha).none())
        if(form.autenticar(email, senha)):
            return redirect('/cms/index/')
    return render(request, template_name, context)



def index(request):
    return render(request, 'oferta/index.html')


def cadastroProfessor(request):
    context = {}

    if request.method == 'POST':
        #salvar os dados nesse ponto
        form = ProfessorForm()
        tiposProfessor = form.carregarTipoProfessor()
        nome  = request.POST.get('nome')
        print(nome + '\n')
        matricula = request.POST.get('matricula')
        print(matricula + '\n')
        idProfessor = request.GET.get('editar')
        print(str(idProfessor) + '\n')


        for tipo in tiposProfessor:
            idTipoProfessor = request.POST.get(str(tipo.id_tipo_professor))
            print(str(idTipoProfessor) + '\n')
            if (idTipoProfessor == str(tipo.id_tipo_professor) or idTipoProfessor == 'on'):
                tipoProfessor = tipo_professor.objects.retornarPorId(tipo.id_tipo_professor).first()
                break

        professorSalvar = professor()

        if idProfessor != None:
            professorSalvar.id_professor = idProfessor

        professorSalvar.ativo = True
        professorSalvar.id_tipo_professor = tipoProfessor
        professorSalvar.nome = nome
        professorSalvar.matricula = matricula

        print('Cheguei no salvar \n')
        form.salvarProfessor(professorSalvar)

        professores = form.carregarProfessoresAlfabetico()

        return redirect('cadastroProfessor')

    else:

        idProfessor = request.GET.get('editar')

        if idProfessor != None:
            form = ProfessorForm()
            tiposProfessor = form.carregarTipoProfessor()
            professores = form.carregarProfessoresAlfabetico()
            professorEditar = form.retornarProfessorPorId(idProfessor)
            context['nome'] = professorEditar.nome
            context['matricula'] = professorEditar.matricula
            for tipo in tiposProfessor:
                if professorEditar.id_tipo_professor.id_tipo_professor == tipo.id_tipo_professor:
                    context[str(tipo.id_tipo_professor)] = tipo.id_tipo_professor
                    context['tipoProf'] = tipo.id_tipo_professor
                    break

        else:
            idProfessor = request.GET.get('excluir')
            if idProfessor != None:
                form = ProfessorForm()
                form.excluirProfessor(form.retornarProfessorPorId(idProfessor))
                tiposProfessor = form.carregarTipoProfessor()
                professores = form.carregarProfessoresAlfabetico()

            else:
                form = ProfessorForm()
                tiposProfessor = form.carregarTipoProfessor
                professores = form.carregarProfessoresAlfabetico()



    context['tiposProfessor'] = tiposProfessor
    context['form'] = form
    context['professores'] = professores
    template_name = 'oferta/cadastroProfessor.html'

    return render(request, template_name, context)

def cadastroDisciplina(request):
    context = {}

    if request.method == 'POST':
        form = DisciplinaForm()
        tiposDisciplina = form.carregarTiposDisciplina()

        nome = request.POST.get('nome')
        print(nome + '\n')

        credito = request.POST.get('credito')
        print(credito + '\n')

        idDisciplina = request.GET.get('editar')
        print(str(idDisciplina) + '\n')

        for tipo in tiposDisciplina:
            idTipoDisciplina = request.POST.get(str(tipo.id_tipo_disciplina))
            print(str(idTipoDisciplina) + '\n')

            if (idTipoDisciplina == str(tipo.id_tipo_disciplina) or idTipoDisciplina == 'on'):
                tipoDisciplina = form.retornarTipoPorId(tipo.id_tipo_disciplina)
                break

        disciplinaSalvar = disciplina()

        if idDisciplina != None:
            disciplinaSalvar.id_disciplina = idDisciplina

        disciplinaSalvar.nome = nome
        disciplinaSalvar.creditos = credito
        disciplinaSalvar.id_tipo_disciplina = tipoDisciplina
        disciplinaSalvar.ativo = True

        print('Cheguei no salva \n')
        form.salvarDisciplina(disciplinaSalvar)

        disciplinas = form.carregarDisciplinasAlfabetico()

        return redirect('cadastroDisciplina')

    else:

        idDisciplina = request.GET.get('editar')

        if idDisciplina != None:

            form = DisciplinaForm()
            tiposDisciplina = form.carregarTiposDisciplina()
            disciplinas = form.carregarDisciplinasAlfabetico()
            disciplinaEditar = form.retornarDisciplinaPorId(idDisciplina)

            context['nome'] = disciplinaEditar.nome
            context['credito'] = disciplinaEditar.creditos

            for tipo in tiposDisciplina:
                if disciplinaEditar.id_tipo_disciplina.id_tipo_disciplina == tipo.id_tipo_disciplina:
                    context[str(tipo.id_tipo_disciplina)] = tipo.id_tipo_disciplina
                    context['tipoDis'] = tipo.id_tipo_disciplina
                    break

        else:

            idDisciplina = request.GET.get('excluir')

            if idDisciplina != None:
                form = DisciplinaForm()
                form.excluirDisciplina(idDisciplina)
                tiposDisciplina = form.carregarTiposDisciplina()
                disciplinas = form.carregarDisciplinasAlfabetico()

            else:
                form = DisciplinaForm()
                tiposDisciplina = form.carregarTiposDisciplina()
                disciplinas = form.carregarDisciplinasAlfabetico()



    context['tiposDisciplina'] = tiposDisciplina
    context['disciplinas'] = disciplinas
    context['form'] = form
    template_name = 'oferta/cadastroDisciplina.html'

    return render(request,template_name,context)


def cadastroCargo(request):
    context = {}

    if request.method == 'POST':
        form = CargoForm()

        nome = request.POST.get('nome')
        print(nome + '\n')

        pontos = request.POST.get('ponto')
        print(pontos + '\n')

        idCargo = request.GET.get('editar')
        print(str(idCargo) + '\n')


        cargoSalvar = cargo()

        if idCargo != None:
            cargoSalvar.id_cargo = idCargo

        cargoSalvar.nome = nome
        cargoSalvar.pontos = pontos
        cargoSalvar.ativo = True

        print('Cheguei no salva \n')
        form.salvar(cargoSalvar)

        cargos = form.carregarCargosAlfabetico()

        return redirect('cadastroCargo')

    else:

        idCargo = request.GET.get('editar')

        if idCargo != None:

            form = CargoForm()
            cargos = form.carregarCargosAlfabetico()
            cargoEditar = form.retornarCargoPorId(idCargo)

            context['nome'] = cargoEditar.nome
            context['ponto'] = str(cargoEditar.pontos)
            print(str(cargoEditar.pontos) + '\n')
        else:

            idCargo = request.GET.get('excluir')

            if idCargo != None:
                form = CargoForm()
                form.excluir(idCargo)
                cargos = form.carregarCargosAlfabetico()

            else:
                form = CargoForm()
                cargos = form.carregarCargosAlfabetico()

    context['cargos'] = cargos
    context['form'] = form
    template_name = 'oferta/cadastroCargo.html'

    return render(request, template_name, context)


def professorDisciplinaPasso1(request):

    context = {}
    form = RankingForm()

    if request.method == 'POST':

        ordena = request.POST.get('ordena')

        print(ordena + 'PRINT AQUI')

        if ordena == 'alf':

            ranks = form.carregarRankingAlfabetico()

        else:

            if ordena == 'pontosasc':

                ranks = form.carregarRankingPontuacaoAsc()

            else:

                if ordena == 'pontosdesc':

                    ranks = form.carregarRankingPontuacaoDesc()

                else:
                    print('ERRO NO ranking')

    else:

        ranks = form.carregarRankingAlfabetico()


    context['ranks'] = ranks
    context['form'] = form
    template_name = 'oferta/vinculoProfessorDisciplina.html'

    return render(request, template_name, context)
