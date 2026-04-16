salarios = [3000.0, 6000.0, 9900.00, 240.00, 1000.00]
for sala in salarios:
    if sala <= 2000.00:
        imposto = sala * 0.10
        percentual = "10%"
    else:
        imposto = sala * 0.20
        percentual = "20%"
    sobra = sala - imposto
    print(f"salário {sala}, e foi cobrado {percentual}, de imposto")