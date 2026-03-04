usuario = input("Digite seu usuario: ")
senha = int(input("DIgite sua senha: "))

if (usuario == "admin" or usuario == "root") and senha == 1234:
    print("acesso liberado")

else:
    print("acesso negado")
