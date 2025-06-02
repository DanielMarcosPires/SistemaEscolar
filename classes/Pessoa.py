from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self,nome,idade):
        self._nome = nome
        self._idade = idade

    @abstractmethod
    def get_nome(self):
        return self._nome
    
    @abstractmethod
    def get_idade(self):
        return self._idade
