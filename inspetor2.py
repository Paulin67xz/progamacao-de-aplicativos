print ("Para operar a prensa hidraulica o aprendiz precisa do curso e supervisão ")

curso = input ("Você concluiu o curso de segurança? s/n" )

if curso == "n":
    print: ("Acesso negado")
elif curso == "s":
     instrutor = input("O instrutor esta presente? s/n ")
     if instrutor == "s":
        print("Acesso liberado")
    elif instrutor == "n":
        print("Aguarde o instrutor")
