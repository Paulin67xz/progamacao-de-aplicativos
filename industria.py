id_usuario = int(input("Digite o seu ID: "))
temperatura = float(input("Qual a temperatura: "))
tempo = int(input("Quanto tempo tem de uso: "))

if (id_usuario % 3 == 0) and (temperatura > 40 or tempo_uso > 8):
    print(f"Funcionario {id_usuario}, você foi escalado para a manutenção preventiva hoje" )
else: 
    print(f"Funcionario {id_usuario}, sua maquina opera dentro dos padrões normais")
