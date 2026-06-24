def  converter_km_para_ms(velocidade_km):
    if velocidade_km > 80:
       velocidade_ms = velocidade_km / 3.6
       return f" sua velocidade é {velocidade_ms} ms.  Reduza" 
    return "velocidade normal"

velocidade = int(input("Qual é a sua velocidade: "))
msg = converter_km_para_ms (velocidade)
print(msg) 
    