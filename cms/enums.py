from enum import Enum

class PontosDisciplina(Enum):
    DISCIPLINA_DIURNO = 1
    DISCIPLINA_NOTURNO = 2
    PROJETO_GRADUACAO = 0.5
    PROJETOS_OUTROS = 0.5
    PROJETO_MESTRADO = 1
    PROJETO_DOUTORADO = 6
    PERIODICO_A1 = 1
    PERIODICO_A2 = 0.75
    PERIODICO_B1 = 0.5
    PERIODICO_B2 = 0.25
    PERIODICO_OUTROS = 0.05


class TipoDisciplina(Enum):
    GRADUACAO = 3
    TRABALHO_GRADUACAO = 4
    PROJETO_LICENCIATURA = 5
    INICIACAO_CIENTIFICA = 6
    MESTREDO = 7
    DOUTORADO = 8
    A1 = 9
    A2 = 10
    B1 = 11
    B2 = 12
    B3_B5 = 13