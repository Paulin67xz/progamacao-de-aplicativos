import sqlite3
def cadastrar_turma(nome, id_serie, id_prof): 
    conexao = sqlite3.connect('sistema_escola.bd')
    cursor = conexao.cursor()
    cursor.execute( "PRAGMA foreign_keys = ON;")
     
