import os
from classes.Professor import Professor
from classes.Aluno import Aluno
from classes.SisGE import SisGE

os.system("cls")

escola = SisGE(
    nome="Uninove"
)
print("*".center(50,"*"))
print(escola.get_nome())
print(escola.get_alunos())
print(escola.get_professores())
print(escola.get_secretarias())
print("*".center(50,"*"))

    