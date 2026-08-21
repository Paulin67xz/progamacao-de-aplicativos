import sqlite3 
 
def criar_tabelas(): 
    conexao = None 
    try: 
        conexao = sqlite3.connect("veiculos.db") 
        cursor = conexao.cursor() 
        cursor.execute("PRAGMA foreign_keys = ON") 
 
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS montadoras ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                marca TEXT, 
                pais_origem TEXT NOT NULL 
            ) 
        """) 
 
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS concessionarias ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                cidade TEXT NOT NULL, 
                id_montadora INTEGER NOT NULL, 
                FOREIGN KEY (id_montadora) 
                    REFERENCES montadoras(id) 
                ) 
         
                       """) 
 
        conexao.commit() 
         
 
    except sqlite3.Error as erro: 
        print(f"Erro no banco de dados: {erro}") 
    except Exception as erro: 
        print(f"Erro inesperado: {erro}") 
    finally: 
        if conexao: 
            conexao.close() 
 
 
 
 
def cadastrar_montadoras(marca, pais_origem): 
    conexao = None 
    try: 
        conexao = sqlite3.connect('veiculos.db') 
        cursor = conexao.cursor() 
     

        cursor.execute(''' 
                        INSERT INTO montadoras (marca, pais_origem) 
                        VALUES (?, ?) 
                        ''', (marca, pais_origem)) 
 
        conexao.commit() 
        return "cadastro realizado"


    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
    except ValueError: 
        print("Valor inválido.") 
    except TypeError: 
        print("Tipo de dado inválido.") 
    except Exception as e: 
        print(f"Erro inesperado: {e}") 
    finally: 
         if conexao: 
             conexao.close() 
 
def listar_montadoras(): 
    conexao = None 
    try: 
 
        conexao = sqlite3.connect('veiculos.db') 
        cursor = conexao.cursor() 
 
        cursor.execute("SELECT * FROM montadoras")  
        listar_montadoras = cursor.fetchall() 
 
        print("=== Lista de Montadoras ===") 
 
        for montadora in listar_montadoras: 
            print(f"ID: {montadora[0]}") 
            print(f"Marca: {montadora[1]}") 
            print(f"país de origem: {montadora[2]}") 
            print("-" * 30)
        conexao.commit()
        return "listado com sucesso"
 
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
    except IndexError: 
        print("Índice fora da lista.") 
    except Exception as e: 
        print(f"Erro inesperado: {e}") 
    finally: 
        if conexao: 
            conexao.close() 
 
def atualizar_montadoras(id_montadora, marca_atualizada, pais_origem_atualizada): 
    conexao = None 
    try: 
 
        conexao = sqlite3.connect('veiculos.db') 
        cursor = conexao.cursor() 
 
        listar_montadoras() 
 
        cursor.execute(f'''SELECT marca , pais_origem FROM montadoras WHERE id = {id_montadora} ''') 
 
        montadora = cursor.fetchone() 
 
        if not montadora: 
            print("Montadora não encontrada") 
            return 
        else: 
            cursor.execute(f''' 
                           UPDATE montadoras  
                           SET marca = '{marca_atualizada}', pais_origem = '{pais_origem_atualizada}' 
                           WHERE id = {id_montadora} 
                           ''') 
             
            conexao.commit() 
            return " Dados alterados "
 
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
    except ValueError: 
        print("Valor inválido.") 
    except TypeError: 
        print("Tipo de dado inválido.") 
    except Exception as e: 
        print(f"Erro inesperado: {e}") 
    finally: 
        if conexao: 
            conexao.close() 
 
def deletar_montadora(id_montadora): 
    conexao = None 
    try: 
 
        conexao = sqlite3.connect('veiculos.db') 
        cursor = conexao.cursor() 
 
        listar_montadoras() 

        cursor.execute("SELECT * FROM montadoras")  
        
        deletar_montadora = cursor.fetchall() 
        
        if not deletar_montadora:
            return "nao existe o id"
        else:
            cursor.execute(f''' DELETE FROM montadoras WHERE id = {id_montadora}''') 

            conexao.commit() 
            return "Montadora deletada"
 
    except sqlite3.IntegrityError: 
        print("Não é possível deletar a montadora.") 
        print("Existe uma concessionária relacionada a ela.") 
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
    except ValueError: 
        print("Valor inválido.") 
    except TypeError: 
        print("Tipo de dado inválido.") 
    except Exception as e: 
        print(f"Erro inesperado: {e}") 
    finally: 
        if conexao: 
            conexao.close() 
 
 
 
def cadartrar_concessionarias(cidade_concessionaria,  id_montadora): 
     conexao = None 
     try: 
 
        conexao = sqlite3.connect('veiculos.db') 
        cursor = conexao.cursor() 
 
        listar_montadoras() 
       

        cursor.execute(f'''SELECT id FROM montadoras WHERE id = {id_montadora} ''') 
 
        montadora = cursor.fetchone() 
 
        if not montadora: 
            return "Montadora não encontrada"
             
        cursor.execute(''' 
                        INSERT INTO concessionarias (cidade, id_montadora) 
                        VALUES (?, ?) 
                        ''', (cidade_concessionaria, id_montadora)) 
 
            
        conexao.commit() 
        return "Cadastro realizado!"
 
 
     except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
     except ValueError: 
        print("Valor inválido.") 
     except TypeError: 
        print("Tipo de dado inválido.") 
     except Exception as e: 
        print(f"Erro inesperado: {e}") 
     finally: 
         if conexao: 
            conexao.close() 
 
 
def listar_concessionaria(): 
    conexao = None 
    try: 
 
        conexao = sqlite3.connect('veiculos.db') 
        cursor = conexao.cursor() 
 
        cursor.execute(""" 
            SELECT concessionarias.id, 
                   concessionarias.cidade, 
                   montadoras.marca 
            FROM concessionarias 
            INNER JOIN montadoras 
            ON concessionarias.id_montadora = montadoras.id 
        """) 
 
        listar_concessionarias = cursor.fetchall() 
 
        print("=== Lista de Concessionarias ===") 
 
        for concessionaria in listar_concessionarias: 
            print(f"ID: {concessionaria[0]}") 
            print(f"Cidade: {concessionaria[1]}") 
            print(f"Montadora: {concessionaria[2]}") 
            print("-" * 30) 
 
 
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
    except IndexError: 
        print("Índice fora da lista.") 
    except Exception as e: 
        print(f"Erro inesperado: {e}") 
    finally: 
        if conexao: 
            conexao.close() 
 
 
def atualizar_concessionaria(): 
    conexao = None 
    try: 
 
        conexao = sqlite3.connect('veiculos.db') 
        cursor = conexao.cursor() 
 
        listar_concessionaria() 
 
        id_concessionaria = int(input("Qual id deseja atualizar: ")) 
 
        cursor.execute(f'''SELECT cidade, id_montadora FROM concessionarias WHERE id = {id_concessionaria} ''') 
 
        concessionaria = cursor.fetchone() 
 
        if not concessionaria: 
            print("concessionaria não encontrada") 
            return 
         
 
        cidade_atualizada = input(" Atualize a cidade: ") 
        id_montadora_atualizado = int(input(" Atualize o id da montadora: ")) 
 
             
             
        cursor.execute(f'''SELECT id FROM montadoras WHERE id = {id_montadora_atualizado} ''') 
 
        montadora = cursor.fetchone() 
 
        if not montadora: 
            print("Montadora não encontrada") 
            print("Digite o ID de uma montadora existente.") 
            return 
 
        cursor.execute(f''' 
                           UPDATE concessionarias 
                            SET cidade = '{cidade_atualizada}', 
                            id_montadora = {id_montadora_atualizado} 
                            WHERE id = {id_concessionaria} 
                            ''') 
         
 
        conexao.commit() 
        print("Dados alterados!") 
             
 
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
    except ValueError: 
        print("Valor inválido.") 
    except TypeError: 
        print("Tipo de dado inválido.") 
    except Exception as e: 
        print(f"Erro inesperado: {e}") 
    finally: 
        if conexao: 
            conexao.close() 
 
def deletar_concessionaria(): 
    conexao = None 
    try: 
 
        conexao = sqlite3.connect('veiculos.db') 
        cursor = conexao.cursor() 
 
        listar_concessionaria() 
 
        id_concessionaria = int(input("Qual id deseja deletar: ")) 
 
        cursor.execute(f''' DELETE FROM concessionarias WHERE id = {id_concessionaria}''') 
 
        conexao.commit() 
        print(" Concessionaria deletada") 
 
 
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
    except ValueError: 
        print("Valor inválido.") 
    except TypeError: 
        print("Tipo de dado inválido.") 
    except Exception as e: 
        print(f"Erro inesperado: {e}") 
    finally: 
        if conexao: 
            conexao.close() 
 
 
 
 
 
 
def menu_montadoras_e_concessionarias(): 
    try: 
       
        while True: 
            print("\n--- TABELA MONTADORAS ---") 
            print("1. Cadastrar Montadora")  
            print("2. Listar Montadoras")  
            print("3. Atualizar Montadora")  
            print("4. Excluir Montadora")  
 
            print("\n--- TABELA CONCESSIONARIAS ---") 
            print("5. Cadastrar Concessionaria")  
            print("6. Listar Concessionarias")  
            print("7. Atualizar Concessionaria")  
            print("8. Excluir Concessionaria")  
             
            print("9. Sair") 
 
            opcao = input("Escolha uma opção: ") 
 
            if opcao == '1': 
                marca = input("Digite a marca da montadora: ") 
                pais_origem = input("Digite o país de origem: ") 
                cadastrar_montadoras(marca,pais_origem) 

            elif opcao == '2': 
               
                listar_montadoras()  

            elif opcao == '3': 
                id_montadora = int(input("Qual id deseja atualizar: "))
                marca_atualizada = input(" Atualize a marca: ")
                pais_origem_atualizada = input(" Atualize o país de origem: ") 
                atualizar_montadoras(id_montadora, marca_atualizada, pais_origem_atualizada) 

            elif opcao == '4': 
                id_montadora = int(input("Qual id deseja deletar: "))
                deletar_montadora(id_montadora)  
 
            elif opcao == '5': 
                cidade_concessionaria = input("Digite a cidade da sua concessionaria: ") 
                id_montadora = int(input("Digite o ID da montadora: ")) 
                cadartrar_concessionarias(cidade_concessionaria, id_montadora) 

            elif opcao == '6': listar_concessionaria() 
            elif opcao == '7': atualizar_concessionaria()  
            elif opcao == '8': deletar_concessionaria()  
            elif opcao == '9': break 
            else: print("Opção inválida!") 
 
    except ValueError: 
        print("Valor inválido.") 
    except TypeError: 
        print("Tipo de dado inválido.") 
    except Exception as e: 
        print(f"Erro inesperado: {e}") 
 
 
criar_tabelas() 
menu_montadoras_e_concessionarias()

assert cadastrar_montadoras ("cm", "cm.ww") == "cadastro realizado"
assert listar_montadoras == "listado com sucesso"
assert atualizar_montadoras (4, "ls", "ls.ww") == " Dados alterados "
assert deletar_montadora(6) == "Montadora deletada"
assert deletar_montadora(2) == "nao existe o id"
assert cadartrar_concessionarias ("cc", "cc.ww") == "Cadastro realizado!"
assert cadartrar_concessionarias ("ac", "ac.ww") == "Montadora não encontrada"














       