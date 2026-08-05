import sqlite3
def conectar():
    conexao = sqlite3.connect("hospital.db")
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao


def criar_tabelas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS hospitais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            crm TEXT NOT NULL,
            id_hospital INTEGER NOT NULL,
            FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
        )
        """)

        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar as tabelas:", erro)
    finally:
        conexao.close



def cadastrar_hospital():
    try:

        conexao = conectar()
        cursor = conexao.cursor()

        nome_hospital = input("Nome do hospital: ")
        cidade = input("Cidade: ")


        comando_inserir = f'''
        INSERT INTO hospitais (nome, cidade)
        values ('{nome_hospital}', '{cidade}')
        '''

        cursor.execute(comando_inserir)

        conexao.commit()

        print("Hospital cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao cadastrar hospital:", erro)
    finally:
        conexao.close


def listar_hospitais():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM hospitais")
        hospitais = cursor.fetchall()

        print("\nHOSPITAIS")
        print("-" * 30)

        for hospital in hospitais: 
            print(f"nome do hospital: {hospital[0]}")
            print(f"cidade: {hospital[1]}")
            print("-" * 30)


    except sqlite3.Error as erro:
        print("Erro ao listar hospitais:", erro)
    finally:
        conexao.close

def atualizar_hospitais():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        listar_hospitais()

        id_hospital = int(input(" Qual seu ID: "))

        cursor.execute(f'''SELECT nome , cidade FROM hospitais WHERE id = {id_hospital} ''')

        hospital = cursor.fetchone()

        if not hospital:
            print(" Não encontrado ")
            conexao.close()
            return
        else:
            
            atualize_nome_hospital = input(" Atualize o hospital: ")
            atualize_cidade = input(" Atualize sua cidade: ")

            cursor.execute(f'''
                            UPDATE hospitais
                            SET nome ='{atualize_nome_hospital}', cidade ='{atualize_cidade}',
                            WHERE id = {id_hospital}
                        ''')
            
            conexao.commit()
            print(" Dados alterados ")

    except sqlite3.Error as erro:
        print("Erro ao atualizar hospitais:", erro)
    finally:
        conexao.close


def deletar_hospital():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        listar_hospitais

        id_hospital = input("Qual hospital deseja deletar: ")

        cursor.execute(f'''DELETE FROM hospitais WHERE Id = {id_hospital}''')

        conexao.commit()
        print("professor deletado")

    except sqlite3.Error as erro:
        print("Erro ao deletar hospitais:", erro)
    finally:
        conexao.close


def menu():
    try:
      
        while True:
            print("\n--- TABELA HOSPITAIS ---")
            print("\n=== SISTEMA HOSPITAL ===")  
            print("1. Cadastrar hospital") 
            print("2. Listar hospitais") 
            print("3. Atualizar hospital") 
            print("4. Excluir hospital") 
            print("5. Sair")
                
            opcao = input("Escolha uma opção: ")

            if opcao == '1': cadastrar_hospital()
            elif opcao == '2': listar_hospitais() 
            elif opcao == '3': atualizar_hospitais() 
            elif opcao == '4': deletar_hospital() 
            elif opcao == '5': break
            else: print("Opção inválida!")

    except sqlite3.Error as erro:
        print("Erro ao deletar hospitais:", erro)

    menu()


