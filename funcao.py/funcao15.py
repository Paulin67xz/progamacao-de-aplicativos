rua = input("Qual é a rua onde você mora: ")
numero = int(input("Qual o numero da sua casa: "))
bairro = input("Qual o nome do seu bairro: ")
cidade = input("Qual o nome da sua cidade: ")
cep = int(input("Qual o CEP da sua casa: "))

def gerar_etiqueta(rua, numero, bairro, cidade, cep):
    return f"RUA: {rua}, Nº: {numero} - BAIRRO: {bairro} - CIDADE: {cidade} - CEP: {cep}"

msg = gerar_etiqueta (rua, numero, bairro, cidade, cep)
print (msg)