import sqlite3 

def inicializa_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS escolas (
                   id INTERGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL
                   )
                   ''')
    
    conexao.commit()
    conexao.close()
    # não foi criado o banco de dados
    # não esta salvando as informações pois não colocaram o conexao.commit() que a variavel que salva as informações no banco