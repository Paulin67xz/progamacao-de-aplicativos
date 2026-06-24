lista_compras = [150.0, 80.0, 200.0, 50.0]
lista_desc = []

def aplicar_promocao (lista, nova_lista):
    for item in lista:
        if lista > 100.0:
            desconto = lista * 0.15
            novo_valor = lista - desconto

