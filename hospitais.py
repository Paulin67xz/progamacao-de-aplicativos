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

def atualizar_professores():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
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
            
            nome_hospital = input(" Atualize o hospital: ")
            cpf_atualizado = input(" Atualize sua cidade: ")

            
