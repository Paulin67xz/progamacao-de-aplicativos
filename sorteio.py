# SORTEIO DE FIDELIDADE

# IDENTIFICAÇÃO

id_usuario = int(input("Digite seu ID de usuario: "))
valor = float(input("Digite o valor da sua compra: ")) 

# REGRAS

if id_usuario % 2 == 0 and valor > 500:
    print(f"Parabens, usuario {id_usuario}. Você ganhou um cupom para sua compra de R$ {valor:.2f}.")
else:
    print(f"Obrigado pela compra, usúario {id_usuario}. Continue acompanhando nossas promoções!")
