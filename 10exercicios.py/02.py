def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"

assert situacao_aluno(6.1) == "Aprovado"

# o 6 e o 5.9 são casos limites porque estão exatamente entre aprovar e reprovar