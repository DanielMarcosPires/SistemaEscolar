class SisGE:
    def __init__(self, nome):
        self._nome = nome
        self._alunos = []
        self._professores = []
        self._secretarias = []

    def get_nome(self):
        return f"Escola: {self._nome}"
    
    def get_alunos(self):
        return f"Alunos: {self._alunos}"
    
    def get_professores(self):
        return f"Professores: {self._professores}"
    
    def get_secretarias(self):
        return f"Secretarias: {self._secretarias}"
