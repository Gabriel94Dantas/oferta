from django.db import models

# Create your models here.
class usuario_manager(models.Manager):

    def retornarTodos(self):
        return self.all()

    def retornarPorId(self,query):
        return self.get_queryset().filter(
            id_usuario__exact = query
        ).first()
    def autenticacao(self, email, senha):
        return self.get_queryset().filter(
            email__exact = email,
            senha__exact = senha
            )



class usuario (models.Model):
    id_usuario = models.AutoField(primary_key = True)
    nome = models.CharField('Nome', max_length = 500)
    email = models.CharField('Descrição do Relacionamento Característica Tarefa', max_length = 500)
    senha = models.CharField('Onde será salva a senha no banco de dados', max_length = 500)
    ativo = models.BooleanField(default=True)
    objects = usuario_manager()


class perfil (models.Model):
    id_perfil = models.AutoField(primary_key = True)
    descricao = models.CharField('Descrição do perfil', max_length = 500)
    ativo = models.BooleanField(default=True)

class perfil_usuario(models.Model):
    id_perfil = models.ForeignKey(perfil, related_name='perfil')
    id_usuario = models.ForeignKey(usuario, related_name = 'usuario')

class tipo_professor_manager(models.Manager):
    def retornarTodos(self):
        return self.all()

    def retornarPorId(self, query):
        return self.get_queryset().filter(
            id_tipo_professor__exact = query
            )

class tipo_professor(models.Model):
    id_tipo_professor = models.AutoField(primary_key = True)
    descricao = models.CharField('Descricao do tipo de professor', max_length = 500)
    ativo = models.BooleanField(default=True)
    objects = tipo_professor_manager()

class tipo_disciplina_manager(models.Manager):

    def retornarTodos(self):
        return self.all()

    def retornarPorId(self,query):
        return self.get_queryset().filter(
            id_tipo_disciplina__exact = query
        ).first()

class tipo_disciplina(models.Model):
    id_tipo_disciplina = models.AutoField(primary_key = True)
    descricao = models.CharField('Descricao do tipo de disciplina', max_length = 500)
    ativo = models.BooleanField(default = True)
    objects = tipo_disciplina_manager()

class professor_manager(models.Manager):

    def editarProfessores(self,query,professorEditar):
        self.filter(id_professor__exact = query)\
            .update(id_professor = professorEditar.id_professor, nome = professorEditar.nome,
                    matricula = professorEditar.matricula, id_tipo_professor = professorEditar.id_tipo_professor,
                    ativo = True)

    def excluirProfessor(self,query):
        self.filter(id_professor__exact = query).delete()

    def retornarTodosProfessoresAlfabetico(self):
        return self.all().order_by('nome')

    def retornarPorId(self,query):
        return self.filter(
            id_professor__exact = query
        ).first()

class professor(models.Model):
    id_professor = models.AutoField(primary_key=True)
    nome = models.CharField('Nome do professor', max_length=500)
    matricula = models.CharField('Matricula do professor', max_length=500)
    id_tipo_professor = models.ForeignKey(tipo_professor, related_name='tipo_professor')
    ativo = models.BooleanField(default=True)
    objects = professor_manager()

class disciplina_manager(models.Manager):

    def editarDisciplina(self,query,disciplinaEditar):
        self.filter(id_disciplina__exact = query).update(
            id_disciplina = disciplinaEditar.id_disciplina,
            nome = disciplinaEditar.nome,
            creditos = disciplinaEditar.creditos,
            id_tipo_disciplina = disciplinaEditar.id_tipo_disciplina,
            ativo = True
        )

    def excluirDisciplina(self,query):
        self.filter(id_disciplina__exact = query).delete()

    def retornarTodasDisciplinasAlfabetico(self):
        return self.all().order_by('nome')

    def retornarDisciplinaPorId(self,query):
        return self.get_queryset().filter(
            id_disciplina__exact = query
        ).first()

class disciplina (models.Model):
    id_disciplina = models.AutoField(primary_key = True)
    nome = models.CharField('Nome da disciplina', max_length = 500)
    creditos = models.IntegerField('Numero de creditos da disciplina', null=True)
    id_tipo_disciplina = models.ForeignKey(tipo_disciplina, related_name = 'tipo_disciplina')
    ativo = models.BooleanField(default = True)
    objects = disciplina_manager()

class rel_professor_disciplina (models.Model):
    id_rel_professor_disciplina = models.AutoField(primary_key = True)
    id_professor = models.ForeignKey(professor, related_name='professor')
    id_disciplina = models.ForeignKey(disciplina, related_name = 'disciplina')
    semestre = models.IntegerField('Semestre primeiro ou segundo', null =  True)
    ano =  models.IntegerField('Ano gravado', null = True)