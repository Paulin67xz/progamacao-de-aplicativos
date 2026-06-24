cargo = input("seu cargo: ")
codigo = int(input("seu código: "))
botao_emergencia = input("s/n: ")
epi = input("EPI completo? s/n: ")

if (cargo == "Engenheiro" or "Tecnico") and (codigo == 1234 or botao_emergencia == "s") and epi == "s":
    print("Acesso liberado")
else:
    print("acesso negado")