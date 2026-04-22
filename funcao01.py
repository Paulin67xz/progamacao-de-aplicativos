def avaliar_desempenho(nota):
    if nota >= 9:
        return "EXCELENTE"
    elif nota >= 7:
        return "Bom"
    elif nota >= 5:
        return "Regular"
    else:
        return "insuficiente"
    
nota_usuario = int(input("Qual foi sua nota: "))

mensagem = avaliar_desempenho(nota_usuario)

print (mensagem)