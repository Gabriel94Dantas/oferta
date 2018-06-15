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
        for tipo in tiposProfessor:
            idTipoProfessor = request.POST.get(str(tipo.id_tipo_professor))
            print(str(idTipoProfessor) + '\n')
            if idTipoProfessor == 'on':
                tipoProfessor = tipo_professor.objects.retornarPorId(tipo.id_tipo_professor).first()
                break

        professorSalvar = professor()
        professorSalvar.ativo = True
        professorSalvar.id_tipo_professor = tipoProfessor
        professorSalvar.nome = nome
        professorSalvar.matricula = matricula

        print('Cheguei no salvar \n')
        form.salvarProfessor(professorSalvar)

    else:
        form = ProfessorForm()
        tiposProfessor = form.carregarTipoProfessor()

    context['tiposProfessor'] = tiposProfessor
    context['form'] = form
    template_name = 'oferta/cadastroProfessor.html'

    return render(request, template_name, context)
