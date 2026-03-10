codigo = int(input("Qual o codigo pacote? "))
peso = float(input("Digite o peso do pacote: "))

if peso < 5 and (codigo % 10 == 0):
    print(f"Pacote {codigo}: ENTREGA EXPRESSA")
elif peso > 50 :
    print:(f" Pacote {codigo}: CARGA PESADA")