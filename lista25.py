tabuada = int(input("digite um numero para ver a tabuada: "))
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"tabuada do {tabuada}")

for numero in lista_numeros:
    resultado = tabuada * numero
    print(f"{tabuada} x {numero} = {resultado}")

