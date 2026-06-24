import sqlite3
def cadastrar():
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
                    idade INTERGER,
                    cpf TEXT UNIQUE NOT NULL
                    cidade TEXT,
                    endereco TEXT,
                    estado TEXT,
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


        # 4. INSERÇÃO DIRETA: Colocando as variáveis direto dentro do texto SQL (F-String)
        comando_inserir = f'''
            INSERT INTO  alunos (nome, telefone, turma, idade, cpf)
            values ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}', '{ cidade_aluno}', '{endereco_aluno}', '{estado_aluno}')
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
        except KeyError:	
            print("Chave não encontrada em dicionário.")
        except AttributeError:	
            print("Objeto não possui o atributo/método usado.")
        except ZeroDivisionError:	
            print("Tentativa de dividir por zero.")
        except FileNotFoundError:	
            print("Arquivo não encontrado.")
        except PermissionError:	
            print("Sem permissão para acessar arquivo/recurso.")
        except ImportError:	
            print("Erro ao importar algo de um módulo.")
        except ModuleNotFoundError:	
            print("Módulo não encontrado.")
        except RuntimeError:	
            print("Erro genérico em tempo de execução.")
        except OverflowError:	
            print("Número excedeu o limite suportado.")
        except MemoryError:	
            print("Memória insuficiente.")
        except KeyboardInterrupt:	
            print("Usuário interrompeu o programa (Ctrl+C).")
        except EOFError:	
            print("Fim inesperado da entrada de dados.")
        except Exception:	
            print("Classe base da maioria dos erros.")
        finally:
            conexao.close
        


def listar():
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

            print("-" * 30)





def alterar():
    try:
        listar()

        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        id_aluno = int(input(" Qual seu ID: "))

        cursor.execute(f'''SELECT * FROM alunos WHERE id = {id_aluno}''')
        
        aluno = cursor.fetchone()

        if not id_aluno:
            print(" Não encontrado ")
            conexao.close()
            return
        else:
            nome_atualizado = input(" Atualize seu nome: ")
            cpf_atualizado = input(" Atualize seu CPF: ")
            telefone_atualizado = input(" Atualize se telefone: ")
            idade_atualizada = input(" Atualize sua idade: ")
            turma_atualizada = input(" Atualize sua turma: ")
            cidade_atualizada = input(" Atualize sua cidade: ")
            endereco_atualizado = input(" Atualize seu endereco: ")
            estado_atualizado = input(" Atualize seu estado: ")
    

            cursor.execute(f'''
                            UPDATE alunos
                            SET nome ='{nome_atualizado}', CPF ='{cpf_atualizado}', Telefone ='{telefone_atualizado}', Idade ='{idade_atualizada}', Turma ='{turma_atualizada}', Cidade ='{ cidade_atualizada}', Endereco ='{endereco_atualizado}', Estado ='{estado_atualizado}'
                        WHERE id ={id_aluno}
                            ''')
            conexao.commit()
            print(" Dados alterados ")

            except ValueError:
                print("Erro de valor no alterar tente novavamente")
            except TypeError:
                print("Erro de tipo de dados")
            except NameError:
                print("Variável não existe.")
            except IndexError:	
                print("Índice fora dos limites da lista.")
            except KeyError:	
                print("Chave não encontrada em dicionário.")
            except AttributeError:	
                print("Objeto não possui o atributo/método usado.")
            except ZeroDivisionError:	
                print("Tentativa de dividir por zero.")
            except FileNotFoundError:	
                print("Arquivo não encontrado.")
            except PermissionError:	
                print("Sem permissão para acessar arquivo/recurso.")
            except ImportError:	
                print("Erro ao importar algo de um módulo.")
            except ModuleNotFoundError:	
                print("Módulo não encontrado.")
            except RuntimeError:	
                print("Erro genérico em tempo de execução.")
            except OverflowError:	
                print("Número excedeu o limite suportado.")
            except MemoryError:	
                print("Memória insuficiente.")
            except KeyboardInterrupt:	
                print("Usuário interrompeu o programa (Ctrl+C).")
            except EOFError:	
                print("Fim inesperado da entrada de dados.")
            except Exception:	
                print("Classe base da maioria dos erros.")
            finally:
                conexao.close
            


def deletar():
    try:

        conexao = sqlite3.connect("escola_demonstracao.db")
        cursor = conexao.cursor()

        listar()

        id_aluno = int(input(" Qual ID deseja deletar: " ))
        
        cursor.execute(f'''DELETE FROM Alunos WHERE Id = {id_aluno}''')
        conexao.commit()
        print("aluno deletado")

        except ValueError:
            print("Erro de valor no deletar tente novavamente")
        except TypeError:
            print("Erro de tipo de dados")
        except NameError:
            print("Variável não existe.")
        except IndexError:	
            print("Índice fora dos limites da lista.")
        except KeyError:	
            print("Chave não encontrada em dicionário.")
        except AttributeError:	
            print("Objeto não possui o atributo/método usado.")
        except ZeroDivisionError:	
            print("Tentativa de dividir por zero.")
        except FileNotFoundError:	
            print("Arquivo não encontrado.")
        except PermissionError:	
            print("Sem permissão para acessar arquivo/recurso.")
        except ImportError:	
            print("Erro ao importar algo de um módulo.")
        except ModuleNotFoundError:	
            print("Módulo não encontrado.")
        except RuntimeError:	
            print("Erro genérico em tempo de execução.")
        except OverflowError:	
            print("Número excedeu o limite suportado.")
        except MemoryError:	
            print("Memória insuficiente.")
        except KeyboardInterrupt:	
            print("Usuário interrompeu o programa (Ctrl+C).")
        except EOFError:	
            print("Fim inesperado da entrada de dados.")
        except Exception:	
            print("Classe base da maioria dos erros.")
        finally:
            conexao.close

def menu():
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

            if opcao == '1': cadastrar()
            elif opcao == '2': listar() 
            elif opcao == '3': alterar() 
            elif opcao == '4': deletar() 
            elif opcao == '5': break
            else: print("Opção inválida!")

            except ValueError:
                print("Erro de valor no menu tente novavamente")
            except TypeError:
                print("Erro de tipo de dados")
            except NameError:
                print("Variável não existe.")
            except IndexError:	
                print("Índice fora dos limites da lista.")
            except KeyError:	
                print("Chave não encontrada em dicionário.")
            except AttributeError:	
                print("Objeto não possui o atributo/método usado.")
            except ZeroDivisionError:	
                print("Tentativa de dividir por zero.")
            except FileNotFoundError:	
                print("Arquivo não encontrado.")
            except PermissionError:	
                print("Sem permissão para acessar arquivo/recurso.")
            except ImportError:	
                print("Erro ao importar algo de um módulo.")
            except ModuleNotFoundError:	
                print("Módulo não encontrado.")
            except RuntimeError:	
                print("Erro genérico em tempo de execução.")
            except OverflowError:	
                print("Número excedeu o limite suportado.")
            except MemoryError:	
                print("Memória insuficiente.")
            except KeyboardInterrupt:	
                print("Usuário interrompeu o programa (Ctrl+C).")
            except EOFError:	
                print("Fim inesperado da entrada de dados.")
            except Exception:	
                print("Classe base da maioria dos erros.")

menu()
   