senha = input("Qual é a sua senha: ")
tentativas = int(input("Qual o numero de tentativas? "))
token = input("Você possui um token? digite S ou N: ")

if senha == "admin123" or (tentativas % 3 == 0 or token == "S"):
    print(f"Tentativa n° {tentativas}: ACESSO CONCEDIDO. ")
else:
    print(f"Tentativa n° {tentativas}: ACESSO BLOQUEADO POR PROTOCOLO. ")