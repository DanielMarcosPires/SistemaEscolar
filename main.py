import os
import re
from classes.Professor import Professor
from classes.Aluno import Aluno
from classes.SisGE import SisGE
from classes.Secretaria import Secretaria
from components.input_com_validacao import input_com_validacao
from components.limite import limite
os.system("cls")

def cadastrarAlunos(escola:SisGE, max:int):
    os.system("cls")
    print("="*20)
    print("(1) - Cadastrar alunos:\n")
    if escola.quantidade_de_alunos() < max:
        nome = input_com_validacao(
            prompt="Informe o nome do aluno \n> ",
            regex=r"^[A-Z][a-z]+(\s[A-Z][a-z]+)+$",
            erro_message="A primeira letra deve ser maiúscula do nome e sobrenome!"
            )
        idade = input_com_validacao(
            prompt="Informe a idade do aluno \n>",
            regex=r"^\d{1,3}$",
            erro_message="A idade deve ser número!"
            )
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
    os.system("cls")
    print("="*20)
    print('(2) - Cadastrar professores:\n')
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

def excluirAluno(escola:SisGE):
    os.system('cls')
    print("(3) - Excluir aluno")
    print(f"")
    if escola.quantidade_de_alunos() != 0:
        print(f"({escola.quantidade_de_alunos()}) Alunos:")
        for i, aluno in enumerate(escola.get_alunosList()):
            print(f"{i+1} - {aluno}")
        print("="*10)
        escolha = int(input("Insira o número indicado para deletar:\n> "))
        escola.delete_aluno(escolha-1)
        
        print(escola.get_alunosList())
        print("Aluno deletado!")
    else:print("[Sem alunos na lista!]")

    input("Aperte enter para sair!")

def excluirProfessores(escola:SisGE):
    os.system('cls')
    print("(4) - Excluir professor")
    if escola.quantidade_de_professores() != 0:
        print(f"({escola.quantidade_de_professores()}) Professores:")

        for i, professor in enumerate(escola.get_professoresList()):
            print(f"{i+1} - {professor}")

        escolha = int(input("Insira o número indicado para deletar:\n> "))
        escola.delete_professor(escolha-1)

        print(escola.get_professores())
        print("Professor deletado!")
    else:print("[Sem professores na lista!]")
    input("Aperte enter para sair!")

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

        limite_de_alunos = 3 #Limite máximo de alunos
        limite_de_professores = 2 #Limite máximo de professores

        alunos = limite(quantidade_de_alunos,limite_de_alunos)
        professores = limite(quantidade_de_professores,limite_de_professores)

        print(f"""(1) - Cadastrar alunos - {alunos} 
(2) - Cadastrar professores - {professores} 
(3) - Excluir aluno
(4) - Excluir professor""")
        print('='*20)
        
        opcao = input_com_validacao(
            prompt="Escolha uma opção:\n> ",
            regex=r"\d+$",
            erro_message="Deve ser um número, tente novamente!"
        )

        match int(opcao):
            case 1: cadastrarAlunos(escola, limite_de_alunos)
            case 2: cadastrarProfessores(escola, limite_de_professores)
            case 3: excluirAluno(escola)
            case 4: excluirProfessores(escola)


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
