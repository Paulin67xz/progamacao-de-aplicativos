
import json # serve para salvar os dados em JSON ou converter dados em JSON
import os # serve para ver se o arquivo esta vazio ou não

BANCO_DADOS = 'alunos.json' # aqui ta falando falando(comparando) que CANCO_DADOS é a mesma coisa que 'alunos.json'


def cadastrar(): # aqui você esta criando a função de cadastrar 
    print("\n--- Novo Cadastro ---") # aqui é para mostrar a mensagem no terminal de uma forma organizada 
    
    if os.path.exists(BANCO_DADOS): # aqui esta perguntando se existe dados no nosso arquivo(BANCO_DADOS)
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # aqui estamos abrindo nosso arquivo para uma leitura
            alunos = json.load(f) # aqui lê um arquivo JSON e converte o conteúdo para Python
    else: # aqui é caso não seja nenhum dos casos
        alunos = [] # aqui é uma lista vazia(pode adicionar algo depois)

    novo_aluno = { # uma variavel para armazenar algo
        "nome": input("Nome: "), # é como uma chave("nome") para armazenar oq vai digitar no input
        "telefone": input("Telefone: "), # é como uma chave("telefone) para armazenar oq vai digitar no input
        "turma": input("Turma: "), # é como uma chave("turma") para armazenar oq vai digitar no input
        "idade": int(input("Idade: ")), # é como uma chave("idade") para armazenar oq vai digitar no input
        "cpf": input("CPF: ") # é como uma chave("cpf") para armazenar oq vai digitar no input
    }
    
    alunos.append(novo_aluno) # aqui ta adicionando as informações do novo_aluno na lista alunos

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # aqui abrimos o arquivo para escrita 
        json.dump(alunos, f, indent=4, ensure_ascii=False) # aqui grava a variável alunos dentro de um arquivo JSON
        
    print("Aluno cadastrado com sucesso!") # aqui é mostra uma mensagem se o código ocorrer

def listar(): # aqui você esta criando a função de listar
    print("\n--- Lista de Alunos ---") # aqui é para mostrar a mensagem no terminal de uma forma organizada 
    
    if os.path.exists(BANCO_DADOS): # aqui esta perguntando se existe dados no nosso arquivo(BANCO_DADOS)
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:  # aqui estamos abrindo nosso arquivo para uma leitura
            alunos = json.load(f) # aqui lê um arquivo JSON e converte o conteúdo para Python
    else: # aqui é caso não seja nenhum dos casos
        alunos = []  # aqui é uma lista vazia(pode adicionar algo depois)

    if not alunos:
        print("Nenhum aluno cadastrado.") # aqui é mostra uma mensagem se o código ocorrer
        return # encerra

    for aluno in alunos: # aqui esta percorrendo uma lista que seria "alunos"
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") # aqui é para mostrar a mensagem ou resultado no terminal
    

def atualizar(): # aqui você esta criando a função de atualizar
    print("\n--- Atualizar Aluno ---") # aqui é para mostrar a mensagem no terminal de uma forma organizada
    if not os.path.exists(BANCO_DADOS): # aqui esta perguntando se não existe dados no nosso arquivo(BANCO_DADOS)
        print("Nenhum aluno cadastrado no sistema.") # aqui é mostra uma mensagem se o código ocorrer
        return # encerra

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # aqui estamos abrindo nosso arquivo para uma leitura
        alunos = json.load(f) # aqui lê um arquivo JSON e converte o conteúdo para Python
         
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) # Mostra a mensagem na tela e fica esperando o usuário digitar
    
    for aluno in alunos:  # aqui esta percorrendo uma lista que seria "alunos"
        if aluno['cpf'] == cpf_busca: # aqui esta fazendo uma comparação para saber se o CPF do aluno atual é exatamente igual ao CPF que você está procurando.
            print(f"Editando dados de: {aluno['nome']}") # aqui é mostra uma mensagem se o código ou ação ocorrer
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # aqui serve para atualizar o nome do aluno, mas mantendo o nome antigo caso o usuário aperte Enter sem digitar nada.
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']  # aqui serve para atualizar o telefone do aluno, mas mantendo o nome antigo caso o usuário aperte Enter sem digitar nada.
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']  # aqui serve para atualizar a turma do aluno, mas mantendo o nome antigo caso o usuário aperte Enter sem digitar nada.
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])  # aqui serve para atualizar a idade do aluno, mas mantendo o nome antigo caso o usuário aperte Enter sem digitar nada.
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']  # aqui serve para atualizar o cpf do aluno, mas mantendo o nome antigo caso o usuário aperte Enter sem digitar nada.
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # aqui abrimos o arquivo para escrita 
                json.dump(alunos, f, indent=4, ensure_ascii=False)  # aqui grava a variável alunos dentro de um arquivo JSON
            print("Dados atualizados com sucesso!") # aqui é mostra uma mensagem se o código ou ação ocorrer
            return # encerra
            
    print("Aluno não encontrado.")  # aqui é mostra uma mensagem se o código ou ação não ocorrer

def excluir(): # aqui você esta criando a função de excluir
    print("\n--- Excluir Aluno ---") # aqui é para mostrar a mensagem no terminal de uma forma organizada
    if not os.path.exists(BANCO_DADOS): # aqui esta perguntando se não existe dados no nosso arquivo(BANCO_DADOS)
        print("Nenhum aluno cadastrado no sistema.") # aqui é mostra uma mensagem se o código ou ação ocorrer
        return  # encerra

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # aqui estamos abrindo nosso arquivo para uma leitura
        alunos = json.load(f) # aqui lê um arquivo JSON e converte o conteúdo para Python
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))  # mostra a mensagem na tela e fica esperando o usuário digitar
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] # o objetivo principal aqui é filtrar uma lista, criando uma nova lista que remove um aluno específico com base no seu id.
    
    if len(nova_lista) < len(alunos): # essa linha serve para verificar se a remoção do aluno realmente aconteceu
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # aqui abrimos o arquivo para escrita 
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")  # aqui é mostra uma mensagem se o código ou ação ocorrer
    else: # aqui é caso não seja nenhum dos casos
        print("Aluno não encontrado.") # aqui é mostra uma mensagem se o código ou ação não ocorrer

def menu(): # aqui você esta criando a função de menu 
    if not os.path.exists(BANCO_DADOS): # aqui esta perguntando se não existe dados no nosso arquivo(BANCO_DADOS)
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # aqui abrimos o arquivo para escrita 
            json.dump([], f) # essa linha de código serve para salvar uma lista vazia dentro de um arquivo no formato JSON

    while True: # cria um loop infinito
      print("\n--- Excluir Aluno ---") # aqui é para mostrar a mensagem no terminal de uma forma organizada e tambem para selecionar
      print("\n=== SISTEMA ESCOLAR ===")  # aqui é para mostrar a mensagem no terminal de uma forma organizada e tambem para selecionar
      print("1. Cadastrar Aluno") # aqui é para mostrar a mensagem no terminal de uma forma organizada e tambem para selecionar
      print("2. Listar Alunos") # aqui é para mostrar a mensagem no terminal de uma forma organizada e tambem para selecionar
      print("3. Atualizar Aluno") # aqui é para mostrar a mensagem no terminal de uma forma organizada e tambem para selecionar
      print("4. Excluir Aluno") # aqui é para mostrar a mensagem no terminal de uma forma organizada e tambem para selecionar
      print("5. Sair") # aqui é para mostrar a mensagem no terminal de uma forma organizada e tambem para selecionar
        
      opcao = input("Escolha uma opção: ")  # mostra a mensagem na tela e fica esperando o usuário digitar
        
      if opcao == '1': cadastrar() # aqui seria caso o usuario escolheçe a ação 1 ai levaria para a função posta
      elif opcao == '2': listar() # aqui seria caso o usuario escolheçe a ação 2 ai levaria para a função posta
      elif opcao == '3': atualizar() # aqui seria caso o usuario escolheçe a ação 3 ai levaria para a função posta
      elif opcao == '4': excluir() # aqui seria caso o usuario escolheçe a ação 4 ai levaria para a função posta
      elif opcao == '5': break # e aqui quebra o laço de repedição caso escolha a ação 5
      else: print("Opção inválida!") # aqui é caso não seja nenhum dos casos
menu() # esta chamando função