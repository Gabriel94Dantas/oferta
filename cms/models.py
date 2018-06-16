from django.db import models

# Create your models here.

class usuario (models.Model):
    id_usuario = models.AutoField(primary_key = True)
    email = models.CharField('Descrição do Relacionamento Característica Tarefa', max_length = 500)
    senha = models.CharField('Onde será salva a senha no banco de dados', max_length = 500)
    ativo = models.BooleanField(default=True)

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

class tipo_disciplina(models.Model):
    id_tipo_disciplina = models.AutoField(primary_key = True)
    descricao = models.CharField('Descricao do tipo de disciplina', max_length = 500)
    ativo = models.BooleanField(default = True)

class professor(models.Model):
    id_professor = models.AutoField(primary_key=True)
    nome = models.CharField('Nome do professor', max_length=500)
    matricula = models.CharField('Matricula do professor', max_length=500)
    id_tipo_professor = models.ForeignKey(tipo_professor, related_name='tipo_professor')
    ativo = models.BooleanField(default=True)

class disciplina (models.Model):
    id_disciplina = models.AutoField(primary_key = True)
    nome = models.CharField('Nome da disciplina', max_length = 500)
    creditos = models.IntegerField('Numero de creditos da disciplina', null=True)
    id_tipo_disciplina = models.ForeignKey(tipo_disciplina, related_name = 'tipo_disciplina')
    ativo = models.BooleanField(default = True)

class rel_professor_disciplina (models.Model):
    id_rel_professor_disciplina = models.AutoField(primary_key = True)
    id_professor = models.ForeignKey(professor, related_name='professor')
    id_disciplina = models.ForeignKey(disciplina, related_name = 'disciplina')
    semestre = models.IntegerField('Semestre primeiro ou segundo', null =  True)
    ano =  models.IntegerField('Ano gravado', null = True)