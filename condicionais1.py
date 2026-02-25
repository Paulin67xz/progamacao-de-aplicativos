seu_nome = input("digite seu nome")
sua_altura = float(input("digite sua altura"))

if sua_altura >= 1.50:
    print("Acesso liberado! Divirta-se na na queda livre",seu_nome)
elif sua_altura < 1.50:
    print("Desculpe, você não tem a altura mínima",seu_nome)