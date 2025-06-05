import os
from classes.Professor import Professor
from classes.Aluno import Aluno
from classes.SisGE import SisGE
from classes.Secretaria import Secretaria
from components.input_com_validacao import input_com_validacao
os.system("cls")

def cadastrarAlunos(escola:SisGE):
    os.system('cls')
    print("(1) - Cadastrar alunos")
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

def cadastrarProfessores(escola:SisGE):
    os.system('cls')
    print('(2) - Cadastrar professores:')
    nome = input("Informe o nome do professor\n> ")
    idade = input("Informe a idade do professor\n> ")
    disciplina = input("Informe a disciplina do professor\n> ")
    
    professor = Professor(nome,idade,disciplina)

    escola.set_professor({
        "nome":professor.get_nome(),
        "idade":professor.get_idade(),
        "disciplina":professor.get_disciplina()
    })


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


        print(f"(1) - Cadastrar alunos x{escola.quantidade_de_alunos()} \n(2) - Cadastrar professores x{escola.quantidade_de_professores()}")

        opcao = int(input(""))

        match opcao:
            case 1: cadastrarAlunos(escola)
            case 2: cadastrarProfessores(escola)


secretaria = Secretaria(
    nome="Daniel",
    idade=21,
    registro_funcional="123456"
)

registro = input('Insira o seu Registro Funcional: ')

if registro == secretaria.get_registro_funcional():
    sistemaEscolar()
else: print("Registro incorreto!")
