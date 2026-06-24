cidades = ["São Paulo", "Rio de Janeiro","Curitiba","Belo Horizonte"]
suacidade = input ("Digite o nome da sua cidade: ")

if suacidade in cidades:
    print(f"A cidade {suacidade} esta na posição",cidades.index(suacidade))

else:
    print("ERRO NO SISTEMA")