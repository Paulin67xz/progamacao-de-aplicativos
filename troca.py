a = int(input("Digite o numero A: "))
b = int(input("Digite o numero B: "))
c = ""

print(f"Valores originais A:{a}, B:{b}")

c = a
a = b 
b = c

print(f"Novos valores: A:{a}, B:{b}")