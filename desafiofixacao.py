livros_disponiveis = ["Python Pro", "Banco de dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
print(f"Livros disponiveis agora: {livros_disponiveis}")

cliente = input("Qual livro você gostaria? ")


if  livros_disponiveis in cliente:
    indice = livros_disponiveis.index(cliente)
    livros_emprestados.append(cliente)
    livros_disponiveis.pop(indice)
    print("Empréstimo realizado com sucesso")
    print(f"Lista dos livros atualizadas. Disponiveis: {livros_disponiveis} Emprestados: {livros_emprestados}")
else:
    print("Desculpe o livro não esta disponivel ")

devolucao = input("Digite o livro para devolucão ")

if devolucao in livros_emprestados:
    indice2 = livros_emprestados.index(devolucao)
    livros_disponiveis.append(devolucao)
    livros_emprestados.pop(indice2)
    print("Devolução concluida")
    print(f"Lista dos livros atualizadas. Disponiveis: {livros_disponiveis} Emprestados: {livros_emprestados}")
else:
    print("Este livro não consta como emprestado")

del livros_disponiveis [0:2]
print(f"Relátorio final:", {livros_disponiveis})