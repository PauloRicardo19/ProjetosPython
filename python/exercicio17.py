#litros gastos em uma viagem

tempo = float(input("Qual a duraçao da viagem em horas?: "))
velocidade = float(input("Qual a velocidade do veiculo?: "))
distancia = tempo * velocidade
Li = distancia / 12
print(f"Essa viagem gastou {Li} Litros")