from classes.Aluno import Aluno


class SisGE:
    def __init__(self, nome):
        self._nome = nome
        self._alunos = []
        self._professores = []

    def cadastrar_alunos(self, nomeDoAluno:str, idadeDoAluno:int):
        aluno = Aluno(nomeDoAluno,idadeDoAluno,20)
        print(aluno.get_nome())

    def get_nome(self):
        return f"Escola: {self._nome}"
    
    def get_alunos(self):
        return f"Alunos: {self._alunos}"
    
    def quantidade_de_alunos(self):
        return len(self._alunos)

    def set_aluno(self,aluno):
        self._alunos.append(aluno)

    def get_professores(self):
        return f"Professores: {self._professores}"
    
    def quantidade_de_professores(self):
        return len(self._professores)

    def set_professor(self, professor):
        self._professores.append(professor)
