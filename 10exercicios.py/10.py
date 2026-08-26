def classificar_temperatura(temperatura):
    if classificar_temperatura < 15:
        return"Frio"
    elif classificar_temperatura >= 15 and classificar_temperatura <= 25:
        return "Agradavel"
    else:
     return "Quente"
    

assert classificar_temperatura(14) == "Frio"
assert classificar_temperatura(17) == "Agradavel"
assert classificar_temperatura(23) == "Agradavel"
assert classificar_temperatura(27) == "Quente"
assert classificar_temperatura(10.5) == "Frio"
assert classificar_temperatura(30) == "Quente"


