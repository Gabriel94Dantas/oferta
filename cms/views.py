from django.shortcuts import render
from .forms import ProfessorForm
from .models import tipo_professor
from .models import professor

# Create your views here.

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
