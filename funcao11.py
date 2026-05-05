def calcular_preco_final (valor_base, imposto_percentual, cupom_desconto):
    total = valor_base - imposto_percentual
    total -= cupom_desconto
    if cupom_desconto > total:
        total = 0
        return total
    return total 

valor_base = int(input("Qual é o seu salário? "))
imposto_percentual = int(input("Qual foi o valor do imposto? "))
cupom_desconto = int (input("Qual é o valor do seu cupom? "))

msg = calcular_preco_final (valor_base, imposto_percentual, cupom_desconto)
print (msg)