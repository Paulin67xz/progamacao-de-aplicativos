garrafas = int(input("Qual o numero de garrafas que passaram pela esteira? "))

if garrafas % 500 == 0:
    print("Hora da limpeza: Parar a maquina ")

elif garrafas % 100 == 0:
    print ("Qualidade: Retire a amostra para teste!")

elif garrafas == 500:
    print("Hora da limpeza, e retire a amostra para teste! ")

else:
    print(f"Produção em dia, Garrafas numero {garrafas} processada. ")
