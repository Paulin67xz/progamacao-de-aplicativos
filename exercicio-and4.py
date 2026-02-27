nome = "admin"

codigo = int(input("Digite seu código"))
usuario = input("DIgite seu usuario")

if usuario == "admin" and codigo == 999:
    print("Acesso liberado")
else:
    print("Falha na autenticação")