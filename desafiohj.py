print("BEM VINDO AO SISTEMA DE POUSO! ")

#1. FASE DE IDENTIFICAÇÃO 

drone = int(input("qual o codigo do drone "))
torre = input("possui autorização da torre? s/n ")
if drone == 999 or torre == "s":
    print("permissão concedida ")

    bateria = int(input("qual o nivel da bateria? (0 a 100) "))
    clima = input("como esta o clima? (ensolarado/chuvoso )")
    vento = int(input("qual a velocidade do vento? "))

    if bateria < 10:
        print ("Pouse imediatamente! ")

    elif bateria > 10:
        if (clima == "ensolarado" and vento < 30) or clima == "chuvoso" and vento > 10:
            print (" pouso liberado, você esta pronto")

        else:
            print("pouso negado, tempo ruim")


else:
    print("permissão negada")