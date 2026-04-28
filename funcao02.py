def senha_valida (senha_aprovada):
    while len(senha_aprovada) < 6 :
        print ("Senha válida")
        senha_aprovada = int(input("Digite a senha novamente: "))
        if len(senha_aprovada) >= 6:
            return (True)
        else:
            return (False)
    
senha_usuario = int(input("digite a senha: "))
msg = senha_valida(senha_usuario)
print (msg)
