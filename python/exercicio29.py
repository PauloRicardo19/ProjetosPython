#receba o tipo de investimento 
print ("1 = POUPANÇA, 2 = RENDA FIXA")
Inve = int(input("Qual o tipo de investimento? "))
Valor = float(input("Qual o valor do deposito? "))
if Inve == 1:
    NovoValor = Valor + (Valor * 0.03)
    print ("Em 30 dias a renda vai ser:",NovoValor)
elif  Inve == 2:
    NovoValor = Valor + (Valor * 0.05)
    print ("Em 30 dias a renda vai ser:",NovoValor)
else:
    print ("Insira um tipo de investimento valido.")