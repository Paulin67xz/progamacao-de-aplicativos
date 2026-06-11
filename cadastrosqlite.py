import sqlite3

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

print(f"Passo 3: Dados de {nome_aluno} gravados com sucesso!")


conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()


cursor.execute("SELECT * FROM Alunos")


alunos = cursor.fetchall()


print("Lista de alunos cadastrados:")
for aluno in alunos:
    print(aluno)


conexao.close()