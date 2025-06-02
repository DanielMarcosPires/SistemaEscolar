import os
from classes.Professor import Professor
from classes.Aluno import Aluno
from classes.SisGE import SisGE
from classes.Secretaria import Secretaria
os.system("cls")

escola = SisGE(
    nome="Uninove"
)
secretaria = Secretaria(
    nome="Ana",
    idade=30,
    registro_funcional="123456"
)

print(secretaria.get_nome())
print(secretaria.get_idade())