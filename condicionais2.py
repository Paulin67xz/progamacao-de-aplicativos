ataque = int(input("Poder de ataque do herói"))
defesa = int(input("Poder de defesa do vilão"))

dano = ataque - defesa

if ataque <= defesa:
    print("O vilão bloqueou o ataque, dano: 0",dano)
elif ataque > defesa:
    print("Ataque crítico! Você causou dano ao vilão, o dano causado foi:",dano)