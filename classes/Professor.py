from typing import override
from classes.Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self,nome,idade,disciplina):
        super().__init__(nome,idade)
        self._disciplina = disciplina

    def get_disciplina(self):
        return self._disciplina
    
    
    @override
    def get_nome(self):
        return super().get_nome()
    
    @override
    def get_idade(self):
        return super().get_idade()