open ('viagens.txt', 'w').close()

def adicionar():
    local = input("Qual local gostaria de adicionar: ")

    with open ('viagens.txt', 'a') as caderno:
        caderno.write(local + '\n')
    print("local adicionado")


def lista():
    with open('viagens.txt', 'r') as caderno:
        viagens = caderno.readlines()

        i = 0
        for viagem in viagens:
            print(f"{i} - {viagem.strip()}")
        i += 1


def atualizar ():
    lista()
    id = int(input("Digite local que deseja alterar"))
    novo_local = input("Digite o novo local que deseja alterar: ")

    with open ('viagens.txt', 'r') as caderno:
        linhas = caderno.readlines()
    
    linhas[id] = novo_local + '\n'

    with open ('viagens.txt', 'w') as caderno:
        caderno.writelines(linhas)
    print("Local atualizado")


def deletar():
    lista()
    id = int(input("Digite local que deseja apagar: "))

    with open ('viagens.txt', 'r') as caderno:
        linhas = caderno.readlines()
    
    del linhas[id]

    with open ('viagens.txt', 'w') as caderno:
        caderno. writelines(linhas)
    print("Local removido")


while True:
    print("\n1-Adicionar | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")
    opcao = input("Escolha: ")

    if opcao == '1': adicionar()
    elif  opcao == '2': lista()
    elif  opcao == '3': atualizar()
    elif  opcao == '4': deletar()
    elif  opcao == '5': break