open ('habitos.txt', 'w').close()

def cadastrar():
    habitos = input("Qual habito gostaria de adicionar: ")

    with open ('habitos.txt', 'a') as rotina:
        rotina.write (habitos, '\n')
    print("Habito adicionado")

def revisar():
    with open ('habitos.txt', 'r') as rotina:
        ler = rotina.readlines()
        
        i = 0
        for leitura in ler:
            print(f"{i} - {leitura.strip()}")
        i += 1
        
def ajustar():
    revisar()

    id = int(input("Digite o local que quer editar: "))
    novo_habito = input("Digite o habito que deseja alterar: ")    
        
    with open ('habitos.txt', 'r') as rotina:
        linhas = rotina.readlines()

        linhas[id] = novo_habito + '\n'

        with open ('habitos.txt', 'w') as rotina:
            rotina.writelines(linhas)
    print("Local atualizado")

def deletar():
     revisar()
    
    id = int(input("Digite o habito que deseja apagar: "))




