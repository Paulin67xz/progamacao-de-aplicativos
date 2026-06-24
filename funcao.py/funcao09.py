lista_precos = [100.0, 200.0, 3.0, 50.0, 100.0 ]
total_final = 0

def somar_carrinho (lista_precos, total):
    for produto in lista_precos:
        total += produto
    if total > 500.0:
        desconto = total * 0.10
        total -= desconto
        return total
    return total

msg = somar_carrinho (lista_precos, total_final)
print (msg) 


