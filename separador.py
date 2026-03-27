lista = [1, 4, 5, 6, 8, 12, 56]
pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista de numeros: ", lista)
print("Lista de numeros: ", pares)
print("Lista de numeros: ", impares)  