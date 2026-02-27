temperatura = float(input("Digite a temperatura"))

if temperatura >= 80:
    print("PERIGO! superaquecimento")

elif temperatura >= 50:
    print("Alerta Ventoinhas ligadas no máximo")

elif temperatura < 50:    print("temperatura estavel")