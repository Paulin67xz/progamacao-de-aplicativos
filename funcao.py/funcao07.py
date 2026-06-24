largura = ""
comprimento = ""
tentativas = 0

def calcular_area (largura, comprimento, tentativas):
    while tentativas != 3:
        largura = int(input("Qual é a largura: "))
        comprimento = int(input("Qual é o comprimento: "))
        multiplicacao = largura * comprimento
        print (f"A sua area é {multiplicacao}")
        tentativas += 1 

calcular_area (largura,comprimento,tentativas)