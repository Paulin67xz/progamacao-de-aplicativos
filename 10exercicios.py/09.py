def buscar_nome(lista, nome):
 	return nome in lista

def tem_senha_valida(senha):
 	return len(senha) >= 8

assert buscar_nome([], "Ana") == False
assert buscar_nome(["Ana", "João"], "Ana") == True
assert buscar_nome(["Ana", "João"], "Carlos") == False


assert tem_senha_valida("") == False
assert tem_senha_valida("Gaby") == False
assert tem_senha_valida("Ronaldinho") == True
