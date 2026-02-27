nome_do_cliente = str(input("digite seu nome"))
valor_total_da_compra = float(input("digite o valor"))
distancia_da_entrega = int(input("qual a distancia da entrega em km"))
cupom = input("digite se quer o cupom")
frete = 40
 

if valor_total_da_compra >= 1.000 and cupom == "S":                         
    desconto_vip = valor_total_da_compra * 0.20
    valor_vip = valor_total_da_compra - desconto_vip 
    print("parabéns você ganhou um desconto de 20%. Seu valor agora é:",valor_vip)

elif valor_total_da_compra > 500 and valor_total_da_compra < 1.000 and cupom == "S":
    desconto_padrao = valor_total_da_compra * 0.10
    valor_padrao = valor_total_da_compra - desconto_padrao
     print("parabéns você ganhou um desconto de 10%. Seu valor agora é:",valor_padrao_padrao)

elif distancia_da_entrega <= 50 and valor_vip > 200:
    print("Você ganhou frete gratis")
elif distancia_da_entrega <= 50 and valor_padrao > 200:

elif 
