usuario = "admin"
usuario = "root"
senha = 1234

usuario = input("Digite seu usuario")
senha = int(input("DIgite seu usuario"))

if (usuario == "admin" or usuario == "root") and senha == 1234:
    print("acesso liberado")

else:
    print("acesso negado")
