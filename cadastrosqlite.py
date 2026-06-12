import sqlite3
def cadastrar():
    # 1. CONEXÃO: Abre ou cria o arquivo do banco de dados
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()


    # 2. CRIAÇÃO DA TABELA: Definindo os campos
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS alunos (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                turma TEXT,
                idade INTERGER,
                cpf TEXT UNIQUE NOT NULL
                )
                ''')


    # 3. INFORMAÇÕES DO ALUNO: Criando variáveis
    nome_aluno = input (" Digite o nome do aluno: ")
    telefone_aluno = input (" Digite o telefone do alunos: ")
    turma_aluno = input (" Digite qual a sua turma: ")
    idade_aluno = int(input(" Digite a sua idade: "))
    cpf_aluno = input(" Digite seu CPF: ")


    # 4. INSERÇÃO DIRETA: Colocando as variáveis direto dentro do texto SQL (F-String)
    comando_inserir = f'''
        INSERT INTO  alunos (nome, telefone, turma, idade, cpf)
        values ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}')
        '''

    # Envia o comando completo para o banco de dados
    cursor.execute(comando_inserir)

    # 5. SALVAR E FECHAR
    conexao.commit()

    print("cadastro realizado")

    conexao.close()



def listar():
    # CONEXÃO: Abre ou cria o arquivo do banco de dados
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos") #SELECT: BUSCA OS DADOS ; * SIGINIFICA TRAZER TUDO ; FROM: SIGNIFICA QUE OS DADOS BUSCADOS SERAM DA TABELA ALUNOS
    alunos = cursor.fetchall() #SIGNIFICA QUE VAI PEGAR TODOS OS REGISTROS DA CONSULTA

    print("=== Lista de Aluno ===")

    for aluno in alunos: #O PROGRAMA PERCORRE CADA REGISTRO NA LISTA ALUNOS
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Telefone: {aluno[2]}")
        print(f"Turma: {aluno[3]}")
        print(f"Idade: {aluno[4]}")
        print(f"CPF: {aluno[5]}")
        print("-" * 30)





def alterar():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_aluno = int(input(" Qual seu ID: "))

    cursor.execute(f'''SELECT nome , cpf FROM alunos WHERE id = {id_aluno}''')
    
    aluno = cursor.fetchone()

    if not aluno:
        print(" Não encontrado ")
    else:
        print(f" Nome atual {aluno[0]} ")
        print(f" CPF atual {aluno [1]} ")

        nome_atualizado = input(" Atualize seu nome: ")
        cpf_atualizado = input(" Atualize seu CPF: ")

        cursor.execute(f'''
                        UPDATE alunos
                        SET nome ='{nome_atualizado}', CPF ='{cpf_atualizado}'
                    WHERE id ={id_aluno}
                        ''')
        conexao.commit()
        print(" Dados alterados ")

        conexao.close()


def deletar():


    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    id_aluno = int(input(" Qual ID deseja deletar: " ))

    # Verifica se o aluno existe
    cursor.execute(f'''SELECT id FROM Alunos WHERE Id = {id_aluno}''')
    aluno = cursor.fetchone()

    if not aluno:
        print ("Aluno não encontrado ")
    else:
        cursor.execute(f'''DELETE FROM Alunos WHERE Id = {id_aluno}''')
        conexao.commit()
        print("aluno deletado")

        conexao.close()

listar()
deletar()
    



    



