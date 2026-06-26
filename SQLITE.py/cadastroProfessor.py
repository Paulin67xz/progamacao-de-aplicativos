import sqlite3
def cadastrar_professores():
    try:
    
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
                    escola TEXT NOT NULL,
                    endereco_professor TEXT
                    )
                    ''')


        nome_professor = input (" Digite o seu nome completo: ")
        telefone_professor = input (" Digite o seu telefone: ")
        materia_professor = input (" Digite qual a sua materia: ")
        idade_professor = int(input(" Digite a sua idade: "))
        cpf_professor = input(" Digite seu CPF: ")
        salario_professor = float(input(" Digite o seu salario: "))
        nome_escola_professor = input(" Digite a escola que trabalha atualmente: ")
        endereco_professor = input(" Digite seu endereço: ")
        comando_inserir = f'''
            INSERT INTO  professor (nome, telefone, materia, idade, cpf, salario, escola, endereco_professor)
            values ('{nome_professor}', '{telefone_professor}', '{materia_professor}', '{idade_professor}', '{cpf_professor}', '{salario_professor}', '{nome_escola_professor}', '{endereco_professor}')
            '''

        cursor.execute(comando_inserir)

        conexao.commit()

        print("cadastro realizado")

    except ValueError:
        print("Valor inválido.")
    except TypeError:
        print("Tipo de dado inválido.")
    except IndexError:
        print("Índice fora da lista.")
    except KeyError:
        print("Chave não encontrada.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except PermissionError:
        print("Permissão negada.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        conexao.close


    conexao.close()

def listar_professores():
    try:
  
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
            print(f"Endereço: {prof[8]}")
            print("-" * 30)

    except ValueError:
        print("Valor inválido.")
    except TypeError:
        print("Tipo de dado inválido.")
    except IndexError:
        print("Índice fora da lista.")
    except KeyError:
        print("Chave não encontrada.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except PermissionError:
        print("Permissão negada.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        conexao.close

def atualizar_professores():
    try:

        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        listar_professores()

        id_professor = int(input(" Qual seu ID: "))

        cursor.execute(f'''SELECT nome , cpf , telefone , idade , materia , salario , escola , endereco_professor FROM professor WHERE id = {id_professor}''')
        
        professor = cursor.fetchone()

        if not professor:
            print(" Não encontrado ")
            conexao.close()
            return
        else:
            
            nome_atualizado = input(" Atualize seu nome: ")
            cpf_atualizado = input(" Atualize seu CPF: ")
            telefone_atualizado = input(" Atualize se telefone: ")
            idade_atualizada = int(input(" Atualize sua idade: "))
            materia_atualizada = input(" Atualize sua materia: ")
            salario_atualizado = float(input(" Atualize o seu salario: "))
            escola_atualizada = input(" Atualize a sua escola: ")
            endereco_atualizado = input(" Atualize seu endereço: ")

            cursor.execute(f'''
                            UPDATE professor
                            SET nome ='{nome_atualizado}', cpf ='{cpf_atualizado}', telefone ='{telefone_atualizado}', idade ={idade_atualizada}, materia ='{materia_atualizada}', salario ={salario_atualizado}, escola ='{escola_atualizada}', endereco_professor ='{endereco_atualizado}'
                            WHERE id = {id_professor}
                            ''')
            conexao.commit()
            print(" Dados alterados ")
    except ValueError:
        print("Valor inválido.")
    except TypeError:
        print("Tipo de dado inválido.")
    except IndexError:
        print("Índice fora da lista.")
    except KeyError:
        print("Chave não encontrada.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except PermissionError:
        print("Permissão negada.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        conexao.close


def deletar_professores():
    try:

        conexao = sqlite3.connect("escola_demonstracao.db")
        cursor = conexao.cursor()

        listar_professores()

        id_professor = int(input(" Qual ID deseja deletar: " ))

        cursor.execute(f'''DELETE FROM professor WHERE Id = {id_professor}''')

        conexao.commit()
        print("professor deletado")

    except ValueError:
        print("Valor inválido.")
    except TypeError:
        print("Tipo de dado inválido.")
    except IndexError:
        print("Índice fora da lista.")
    except KeyError:
        print("Chave não encontrada.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except PermissionError:
        print("Permissão negada.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        conexao.close


def menu():
    try:
      
        while True:
            print("\n--- TABELA PROFESSORES ---")
            print("\n=== SISTEMA ESCOLAR ===")  
            print("1. Cadastrar professor") 
            print("2. Listar professor") 
            print("3. Atualizar professor") 
            print("4. Excluir professor") 
            print("5. Sair")
                
            opcao = input("Escolha uma opção: ")

            if opcao == '1': cadastrar_professores()
            elif opcao == '2': listar_professores() 
            elif opcao == '3': atualizar_professores() 
            elif opcao == '4': deletar_professores() 
            elif opcao == '5': break
            else: print("Opção inválida!")

    except ValueError:
        print("Valor inválido.")
    except TypeError:
        print("Tipo de dado inválido.")
    except IndexError:
        print("Índice fora da lista.")
    except KeyError:
        print("Chave não encontrada.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except PermissionError:
        print("Permissão negada.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


menu()
