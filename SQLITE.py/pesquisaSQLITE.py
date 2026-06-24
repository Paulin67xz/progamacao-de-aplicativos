import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

id_aluno = int(input(" Qual seu ID: "))
nome_atualizado = input(" Atualize seu nome: ")
cpf_atualizado = input(" Atualize seu CPF: ")

cursor.execute(f'''
                UPDATE alunos
                SET nome ={nome_atualizado}, CPF ={cpf_atualizado}
               WHERE id ={id_aluno}
                ''')

if not id:
    print( "Sem cadastro")
else:
    print("Nome atualizado e CPF atualizado")

