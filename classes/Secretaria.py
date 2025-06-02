from typing import override
from classes.Pessoa import Pessoa

class Secretaria(Pessoa):
    def __init__(self, nome, idade, registro_funcional):
        super().__init__(nome, idade)
        self._registro_funcional = registro_funcional

    @override
    def get_nome(self):
        return super().get_nome()
    
    @override
    def get_idade(self):
        return super().get_idade()
    
    
