valor = float(input("Digite o valor da compra: "))
prime = input("Você tem prime? s/n: ")
frete = 50.00

if (valor >= 500.00 or prime == "s") and valor > 100.00:
    frete = 00.00
    print("você ganhou frete gratis")
    valor_total = valor + frete
    print("seu valor total é", valor_total) 

else:
    frete = 50.00
    valor_total = valor + frete 
    print("você não ganhou frete gratis")
    print("Seu valor total é", valor_total)