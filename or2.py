media_escolar = float (input("digite sua média"))
renda_familiar = float (input("digite sua renda familiar"))
escola = input ("você veio de escola publica? s/n")

if media_escolar > 8.0 and (renda_familiar < 2.000 or escola == "s"):
    print("você ganhou a bolsa")
    
else media_escolar > 8.0 and (renda_familiar == 2.000 or escola == "n"):
    print("você não ganhou a bolsa")
