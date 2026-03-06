cliente = input ("digite seu nome: ")
valor_original = float(input("digite o valor da compra: R$ "))
distancia_da_entrega = int(input("qual a distancia da entrega em km: "))
cupom = input("Possui cupom? s/n ")

desconto = 0.0
 

if valor_original >= 1000.0 and cupom == "s":                         
    desconto = valor_original * 0.20
elif valor_original  > 500.0 and cupom == "s":
   desconto = valor_original * 0.10

valor_com_desconto = valor_original - desconto

frete = 40.0
if distancia_da_entrega <= 50 and valor_com_desconto > 200.0:
    frete = 0.0

total_final = valor_com_desconto + frete 

print("-" * 30)
print(f"RELATORIO DA COMPRA - {cliente}")
print(f"Valor original: R$ {valor_original:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Frete: R$ {frete:.2f}")
print(f"TOTAL A PAGAR: R$ {total_final:.2f}")

if desconto == (valor_original * 0.20):
    print(" Supresa você ganhou um mouse pad")
print("-"* 30)
