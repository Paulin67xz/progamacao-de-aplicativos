import sqlite3
def cadastrar_alunos():
    try:
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
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    cidade TEXT,
                    endereco TEXT,
                    estado TEXT,
                    id_professor INTEGER,
                    FOREIGN KEY (id_professor) REFERENCES professor(id)
                    )
                    ''')


        # 3. INFORMAÇÕES DO ALUNO: Criando variáveis
        nome_aluno = input (" Digite o nome do aluno: ")
        telefone_aluno = input (" Digite o telefone do alunos: ")
        turma_aluno = input (" Digite qual a sua turma: ")
        idade_aluno = int(input(" Digite a sua idade: "))
        cpf_aluno = input(" Digite seu CPF: ")
        cidade_aluno = input(" Digite sua cidade: ")
        endereco_aluno = input(" Digite seu endereço: ")
        estado_aluno = input(" Digite seu estado: ")
        id_professor = int(input(" Digite o id do seu professor: "))


        # 4. INSERÇÃO DIRETA: Colocando as variáveis direto dentro do texto SQL (F-String)
        comando_inserir = f'''
            INSERT INTO  alunos (nome, telefone, turma, idade, cpf, cidade, endereco, estado, id_professor)
            values ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}', '{ cidade_aluno}', '{endereco_aluno}', '{estado_aluno}', '{id_professor}')
            '''

        # Envia o comando completo para o banco de dados
        cursor.execute(comando_inserir)

        conexao.commit()

        print("cadastro realizado")

    except ValueError:
        print("Erro de valor no cadastro tente novavamente")
    except TypeError:
        print("Erro de tipo de dados")
    except NameError:
        print("Variável não existe.")
    except IndexError:	
        print("Índice fora dos limites da lista.")
    except FileNotFoundError:	
        print("Arquivo não encontrado.")
    # except Exception as error:	
    #     print(f"Classe base da maioria dos erros: {error}.")
    finally:
        print("codigo encerrado")
        conexao.close
        


def listar_alunos():
    try:

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
            print(f"CIDADE: {aluno[6]}")
            print(f"ENDEREÇO: {aluno[7]}")
            print(f"ESTADO: {aluno[8]}")
            print(f"id_professor: {aluno[9]}")

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
    # except Exception as e:
    #     print(f"Erro inesperado: {e}")
    finally:
        print("codigo encerrado")
        conexao.close





def alterar_alunos():
    try:

        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        listar_alunos()
        id_aluno = int(input(" Qual seu ID: "))

        cursor.execute(f'''SELECT * FROM alunos WHERE id = {id_aluno}''')
        
        aluno = cursor.fetchall()

        if not aluno:
            print(" Não encontrado ")
            conexao.close()
            return
        else:
        
            nome_atualizado = input(" Atualize seu nome: ")
            cpf_atualizado = input(" Atualize seu CPF: ")
            telefone_atualizado = input(" Atualize se telefone: ")
            idade_atualizada = int(input(" Atualize sua idade: "))
            turma_atualizada = input(" Atualize sua turma: ")
            cidade_atualizada = input(" Atualize sua cidade: ")
            endereco_atualizado = input(" Atualize seu endereco: ")
            estado_atualizado = input(" Atualize seu estado: ")
            id_professor_atualizado = int(input("Atualize o id do seu professor:"))
    

            cursor.execute(f'''
                            UPDATE alunos
                            SET nome ='{nome_atualizado}', CPF ='{cpf_atualizado}', Telefone ='{telefone_atualizado}', Idade ='{idade_atualizada}', Turma ='{turma_atualizada}', Cidade ='{ cidade_atualizada}', Endereco ='{endereco_atualizado}', Estado ='{estado_atualizado}', id_professor ='{id_professor_atualizado}'
                        WHERE id ={id_aluno}
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
    # except Exception as e:
    #     print(f"Erro inesperado: {e}")
    finally:
        print("codigo encerrado")
        conexao.close
            


def deletar_alunos():
    try:

        conexao = sqlite3.connect("escola_demonstracao.db")
        cursor = conexao.cursor()

        listar_alunos()

        id_aluno = int(input(" Qual ID deseja deletar: " ))
        
        cursor.execute(f'''DELETE FROM Alunos WHERE Id = {id_aluno}''')
        conexao.commit()
        print("aluno deletado")

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
    # except Exception as e:
    #     print(f"Erro inesperado: {e}")
    finally:
        print("codigo encerrado")
        conexao.close


def menu_alunos():
    try:

        while True:
            print("\n--- TABELA ALUNOS ---")
            print("\n=== SISTEMA ESCOLA ===")  
            print("1. Cadastrar aluno") 
            print("2. Listar aluno") 
            print("3. Atualizar aluno") 
            print("4. Excluir aluno") 
            print("5. Sair")
                
            opcao = input("Escolha uma opção: ")

            if opcao == '1': cadastrar_alunos()
            elif opcao == '2': listar_alunos() 
            elif opcao == '3': alterar_alunos() 
            elif opcao == '4': deletar_alunos() 
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
    # except Exception as e:
    #     print(f"Erro inesperado: {e}")

menu_alunos()
   