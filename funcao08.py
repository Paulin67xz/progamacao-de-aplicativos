def contar_caracteres (frase_ou_palavra):
    if len(frase_ou_palavra) < 5:
        return "Nome de usuario muito curto"
    else:
        return "Nome aceito"
    
frase_ou_palavra = input("Digite um nome de usuario para o sistema: ")
msg = contar_caracteres (frase_ou_palavra)
print (msg)