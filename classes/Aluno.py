from typing import override
from classes.Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,nome,idade,matricula):
        self._nome = nome
        self._idade = idade
        self._matricula = matricula

    @override
    def get_nome(self):
        return super().get_nome()
    
    @override
    def get_idade(self):
        return super().get_idade()