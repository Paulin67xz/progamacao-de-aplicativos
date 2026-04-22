def senha_valida (senha_aprovada):
    while len(senha_aprovada) <6 :
        print ("Senha válida")
        senha = int(input("Digite a senha: "))
        if senha > 6:
            return (True)
        else:
            return (False)
    
senha_usuario = int(input("digite a senha: "))
senha_valida = (senha_usuario)