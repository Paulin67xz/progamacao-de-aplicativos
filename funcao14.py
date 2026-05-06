def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
   
    if possui_certificacao == True:
        return True
    
   
    if nota_teste > 80 and anos_xp > 2:
        return True
    else:
        return False

nota = float(input("Digite a nota do teste: "))
anos = int(input("Digite os anos de experiência: "))
cert = input("Possui certificação? (s/n): ")

if cert == "s":
    possui_certificacao = True
else:
    possui_certificacao = False

resultado = verificar_aprovacao(nota, anos, possui_certificacao)

if resultado == True:
    print("Contratar")
else:
    print("Descartar")