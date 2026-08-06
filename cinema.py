import sqlite3

def cadastrar_tabelas():
    try:

        conexao = sqlite3.connect("cinema.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS cinemas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_cinema TEXT NOT NULL,
                        shopping_cinema TEXT NOT NULL
                        )''')


        cursor.execute('''CREATE TABLE IF NOT EXISTS salas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        numero_sala TEXT,
                        capacidade TEXT,
                        id_cinema INTEGER NOT NULL,
                        FOREIGN KEY (id_cinema) REFERENCES cinemas (id)
                        )''')

        conexao.commit() 


    except sqlite3.Error as erro:
            print("Erro:", erro)

    finally: 
        print("Finalizado")
        conexao.close()


def criar_salas():
     try:
          