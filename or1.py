idade = int(input("digite sua idade:"))
ingresso_vip = input("tem ingresso vip? S/N:")
lista =  input("você esta na lista? S/N:")

if idade >= 18 and (ingresso_vip == "S" or lista == "S"):
    print("Acesso liberado")