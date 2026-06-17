import sqlite3
def cadastrar():
    
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()


    
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professor (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                materia TEXT,
                idade INTERGER,
                cpf TEXT UNIQUE NOT NULL,
                salario REAL NOT NULL,
                escola TEXT NOT NULL
                )
                ''')


    nome_professor = input (" Digite o seu nome completo: ")
    telefone_professor = input (" Digite o seu telefone: ")
    materia_professor = input (" Digite qual a sua materia: ")
    idade_professor = int(input(" Digite a sua idade: "))
    cpf_professor = input(" Digite seu CPF: ")
    salario_professor = float(input(" Digite o seu salario: "))
    nome_escola_professor = input(" Digite a escola que trabalha atualmente: ")

    comando_inserir = f'''
        INSERT INTO  professor (nome, telefone, materia, idade, cpf, salario, escola)
        values ('{nome_professor}', '{telefone_professor}', '{materia_professor}', '{idade_professor}', '{cpf_professor}', '{salario_professor}', '{nome_escola_professor}')
        '''

    cursor.execute(comando_inserir)

    conexao.commit()

    print("cadastro realizado")

    conexao.close()

def listar():
  
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM professor") 
    professor = cursor.fetchall()

    print("=== Lista de Professor ===")

    for prof in professor: 
        print(f"ID: {prof[0]}")
        print(f"Nome: {prof[1]}")
        print(f"Telefone: {prof[2]}")
        print(f"Materia: {prof[3]}")
        print(f"Idade: {prof[4]}")
        print(f"CPF: {prof[5]}")
        print(f"Salario: {prof[6]}")
        print(f"Escola: {prof[7]}")
        print("-" * 30)

        conexao.close()

def atualizar():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_professor = int(input(" Qual seu ID: "))

    cursor.execute(f'''SELECT nome , cpf , telefone , idade , materia , salario , escola FROM professor WHERE id = {id_professor}''')
    
    professor = cursor.fetchone()

    if not professor:
        print(" Não encontrado ")
        conexao.close()
        return
    else:
        print(f" Nome atual {professor[0]} ")
        print(f" CPF atual {professor[1]} ")
        print(f" Telefone atual {professor[2]} ")
        print(f" Idade atual {professor[3]} ")
        print(f" Materia atual {professor[4]} ")
        print(f" Salario atual {professor[5]}")
        print(f" Escola atual {professor[6]}")

        nome_atualizado = input(" Atualize seu nome: ")
        cpf_atualizado = input(" Atualize seu CPF: ")
        telefone_atualizado = input(" Atualize se telefone: ")
        idade_atualizada = input(" Atualize sua idade: ")
        materia_atualizada = input(" Atualize sua materia: ")
        salario_atualizado = float(input(" Atualize o seu salario: "))
        escola_atualizada = input(" Atualize a sua escola: ")

        cursor.execute(f'''
                        UPDATE professor
                        SET nome ='{nome_atualizado}', CPF ='{cpf_atualizado}', Telefone ='{telefone_atualizado}', Idade ='{idade_atualizada}', Materia ='{materia_atualizada}', Salario ='{salario_atualizado}', Escola ='{escola_atualizada}'
                    WHERE id ={id_professor}
                        ''')
        conexao.commit()
        print(" Dados alterados ")

        conexao.close()

def deletar():


    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    listar()

    id_professor = int(input(" Qual ID deseja deletar: " ))

    cursor.execute(f'''DELETE FROM professor WHERE Id = {id_professor}''')

    conexao.commit()
    print("professor deletado")

    conexao.close()

def menu():
      
    while True:
        print("\n--- TABELA PROFESSORES ---")
        print("\n=== SISTEMA ESCOLAR ===")  
        print("1. Cadastrar professor") 
        print("2. Listar professor") 
        print("3. Atualizar professor") 
        print("4. Excluir professor") 
        print("5. Sair")
            
        opcao = input("Escolha uma opção: ")

        if opcao == '1': cadastrar()
        elif opcao == '2': listar() 
        elif opcao == '3': atualizar() 
        elif opcao == '4': deletar() 
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()
