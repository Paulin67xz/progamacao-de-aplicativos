valor_total_da_compra =float(input("digite o valor total da compra"))
cupom = input("digite o nome do cupom")
nome_do_cupom = "DEV10"

desconto = valor_total_da_compra * 0.10 
novo_valor = valor_total_da_compra - desconto

if nome_do_cupom == "DEV10":
    print("Cupom aplicado:",novo_valor)
else:
    print("Cupom inválido:",valor_total_da_compra)