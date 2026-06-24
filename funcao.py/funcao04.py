lista_materiais = ["Uva", "Banana", "Martelo", "Prego"]
escolha = input("Escolha um [Uva, Banana, Martelo, Prego] ")

if escolha in lista_materiais:
    print("ENCONTRADO")
else:
    print("Não disponivel")