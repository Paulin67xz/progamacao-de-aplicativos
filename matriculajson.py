import json
import os

MATRICULA = 'alunos.json'

def cadastrar():
    print("\n--- Novo Cadastro ---")

    if os.path.exists(MATRICULA):
        with open(MATRICULA, 'r', encoding='utf-8') as f:
            alunos = json.load(f)
    else:
        alunos = []

    ID_aluno = int(input("Qual é o seu ID"))
    novo_aluno = { 
        "ID": ID_aluno,
        "nome": input("Nome: "), 
        "telefone": input("Telefone: "), 
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ") 
    }          
      
    if len(alunos) !=0:
        for dados in alunos:
            if dados["ID"] == ID_aluno:
                print("ID já possui cadastro! ")
                return

    alunos.append(novo_aluno)
    with open (MATRICULA, 'w', encoding='utf-8') as f :
        json.dump(alunos, f, indent=4)
    print("Aluno cadastrado! ")   


def listar():
    print("\n--- Lista de Alunos ---")

    
    if os.path.exists(MATRICULA):
        with open(MATRICULA, 'r', encoding='utf-8') as f:
            alunos = json.load(f)
    else:
        alunos = []

    if not alunos:
     print("Nenhum aluno cadastrado.")
     return
    
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") # aqui é para mostrar a mensagem ou resultado no terminal
    

def atualizar():
    alunos = carregar_alunos()

    print("\n--- Atualizar Aluno ---") 
    
    id_aluno = int(input("Digite o ID: "))

    for aluno in alunos:

        if aluno["id"] == id_aluno:

            aluno["nome_completo"] = input("Novo nome: ")
            aluno["telefone"] = input("Novo telefone: ")
            aluno["turma"] = input("Nova turma: ")
            aluno["idade"] = int(input("Nova idade: "))
            aluno["cpf"] = input("Novo CPF: ")

            salvar_alunos(alunos)

            print("Aluno atualizado!")
            return

    print("Aluno não encontrado.")



          