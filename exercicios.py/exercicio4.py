nome_do_produto = input ("Digite o produto escolhido")
preço_unitario = float(input("Digite o valor do produto"))
quantidade_do_produto = int(input("Digite a quantidade do produto"))

multiplicacao = preço_unitario * quantidade_do_produto

print("Nome do produto", nome_do_produto)
print("Quantidade adquirida", quantidade_do_produto)
print("Valor unitario", preço_unitario)
print("Valor total a ser pago é:", multiplicacao)