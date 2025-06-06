import os
import re
from classes.Professor import Professor
from classes.Aluno import Aluno
from classes.SisGE import SisGE
from classes.Secretaria import Secretaria
from components.input_com_validacao import input_com_validacao
os.system("cls")

def cadastrarAlunos(escola:SisGE, max:int):
    os.system('cls')
    print("(1) - Cadastrar alunos")
    if escola.quantidade_de_alunos() < max:
        nome = input("Informe o nome do aluno \n> ")
        idade = input("Informe a idade do aluno \n>")
        aluno = Aluno(
            nome=nome,
            idade=idade,
            matricula=0
        )
        escola.set_aluno(
            aluno={
                "nome":aluno.get_nome(),
                "idade":aluno.get_idade()
            }
        )
    else: print("")

def cadastrarProfessores(escola:SisGE, max:int):
    os.system('cls')
    print('(2) - Cadastrar professores:')
    if escola.quantidade_de_professores() < max:
        nome = input("Informe o nome do professor\n> ")
        idade = input("Informe a idade do professor\n> ")
        disciplina = input("Informe a disciplina do professor\n> ")
        
        professor = Professor(nome,idade,disciplina)

        escola.set_professor({
            "nome":professor.get_nome(),
            "idade":professor.get_idade(),
            "disciplina":professor.get_disciplina()
        })
    else: print("")


def sistemaEscolar():
    escola = SisGE(
        nome="Uninove"
    )
    while True:
        os.system('cls')
        print('*'*20)
        print(escola.get_nome())
        print(escola.get_alunos())
        print(escola.get_professores())
        print('*'*20)

        quantidade_de_alunos = escola.quantidade_de_alunos()
        quantidade_de_professores = escola.quantidade_de_professores()

        limite_de_alunos = 2 #Limite máximo de alunos
        limite_de_professores = 2 #Limite máximo de professores

        if quantidade_de_alunos < limite_de_alunos:
            info1 = f"{quantidade_de_alunos} de {limite_de_alunos}"
        else:info1 = f"Atingiu um limite máximo: {quantidade_de_alunos} de {limite_de_alunos}*"

        if quantidade_de_professores < limite_de_professores:
            info2 = f"{quantidade_de_professores} de {limite_de_professores}"
        else:info2 = f"Atingiu um limite máximo: {quantidade_de_professores} de {limite_de_alunos}*"

        print(f"(1) - Cadastrar alunos - {info1} \n(2) - Cadastrar professores - {info2}")
        print('='*20)
        
        opcao = input_com_validacao(
            prompt="Escolha uma opção:\n> ",
            regex=r"\d+$",
            erro_message="Deve ser um número, tente novamente!"
        )

        match int(opcao):
            case 1: cadastrarAlunos(escola, limite_de_alunos)
            case 2: cadastrarProfessores(escola, limite_de_professores)


secretaria = Secretaria(
    nome="Daniel",
    idade=21,
    registro_funcional="123456"
)

print("""
█▀ █ █▀ ▀█▀ █▀▀ █▀▄▀█ ▄▀█   █▀▀ █▀ █▀▀ █▀█ █░░ ▄▀█ █▀█
▄█ █ ▄█ ░█░ ██▄ █░▀░█ █▀█   ██▄ ▄█ █▄▄ █▄█ █▄▄ █▀█ █▀▄
      """)

registro = input_com_validacao(
    prompt='Insira o seu Registro Funcional:\n>  ',
    regex=r"\d{6,12}$",
    erro_message="Acesso negado!"
)

if registro == secretaria.get_registro_funcional():
    sistemaEscolar()
