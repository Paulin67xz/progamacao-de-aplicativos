import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
     DROP TABLE alunos
''')

conexao.commit()


# import sqlite3

# conexao = sqlite3.connect('escola_demonstracao.db')
# cursor = conexao.cursor()

# cursor.execute('''
#      ALTER TABLE professor
#      ADD COLUMN endereco_professor TEXT;
# ''')

# conexao.commit()


# import sqlite3

# conexao = sqlite3.connect('escola_demonstracao.db')
# cursor = conexao.cursor()

# cursor.execute('''
#      ALTER TABLE alunos
#      ADD COLUMN endereco TEXT;
# ''')


# conexao.commit()

# conexao = sqlite3.connect('escola_demonstracao.db')
# cursor = conexao.cursor()

# cursor.execute('''
#      ALTER TABLE alunos
#      ADD COLUMN cidade TEXT;
# ''')

# conexao.commit()


# conexao = sqlite3.connect('escola_demonstracao.db')
# cursor = conexao.cursor()

# cursor.execute('''
#      ALTER TABLE alunos
#      ADD COLUMN estado TEXT;
# ''')

# conexao.commit()
