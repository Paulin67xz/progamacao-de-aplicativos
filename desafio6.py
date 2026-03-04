saldo_inicial = 1000
operacao = input("Qual operação você ira realizar? ")

if operacao == "deposito": 
    deposito = float(input("Qual o valor que você quer depositar? R$: "))
    if deposito > 0:

        valor_final = saldo_inicial + deposito

elif operacao == "saque":
    saque = float(input("Qual o valor que você quer sacar? R$: "))
    if (saque > 0 and saque >= saldo_inicial) or saque == 100.00:
        valor_final = saldo_inicial - saque

elif operacao == "extrato":
    print("seu saldo é: ", saldo_inicial)
    valor_final = saldo_inicial

print("Seu saldo agora é: ", valor_final)