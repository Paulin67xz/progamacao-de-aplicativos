def sofrer_dano(valor_dano, vida):
    while vida > 0:
        if valor_dano > vida:
            return "Game Over"
        vida -= valor_dano
        print (f"Vida restante: {vida}") 
        if vida > 0:
            valor_dano = int(input("Digite o dano do oponente: "))
        else:
            return "Game Over"

valor_vida = int(input(" Qual é o valor da sua vida: "))
valor_dano = int(input("Qual foi o dano: "))
msg = sofrer_dano(valor_dano, valor_vida)
        
        