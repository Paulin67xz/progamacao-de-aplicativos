sua_idade = int(input("Digite sua idade"))
seu_dinheiro = float(input("Digite quanto de dinheiro você tem"))

if sua_idade >= 18 and seu_dinheiro >= 50.0:
    print("Acesso autoriazado! Bem-vindo ao evento")
elif sua_idade < 18 and seu_dinheiro >= 50.0:
    print(" Infelismente voçe não cumpre os requisitos de entrada")
elif sua_idade >= 18 and seu_dinheiro < 50.0:
    print(" Infelismente voçe não cumpre os requisitos de entrada")