print("Logistica de Distribuição (DIVISÃO DE CARGAS) ")

pacote = int(input("Qual é o código do pacote? "))
peso = float(input("Qual é o peso do pacote? "))


print("-----------------------------------------")


if peso < 5 and (pacote % 10 == 0):
    print(f"Pacote {pacote}: ENTREGA EXPRESSA")
elif peso > 50.0:
    print(f"Pacote {pacote}: CARGA PESADA")
else :
    print("INFORMAÇÕES INVALIDAS")