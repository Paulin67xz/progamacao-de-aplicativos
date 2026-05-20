def criar_arquivo():
   open ("dados.json", 'w').close()
criar_arquivo()

inport json

cpf_aluno = int(input("Qual seu CPF: "))
nome_aluno = input("Qual seu nome: ")
telefone_aluno = int(input("Qual seu número: "))
turma = input("Qual a sua turma")
idade_aluno = int(input("Qual a sua idade: "))

aluno = {"cpf": cpf_aluno 
        "nome": nome_aluno
        "telefone": telefone_aluno
        "turma": turma
        "idade": idade_aluno} 