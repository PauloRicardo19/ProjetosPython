#receber tipo de investimento com passagem de parâmetro

investimento: int = 0
valor: float = 0.0

def Tipo_Investimento(I, V):
    NovoValor: float = 0.0
    if I == 1:
        NovoValor = V + (V * 0.03)
        print ("Em 30 dias a renda vai ser:",NovoValor)
    elif I == 2:
        NovoValor = V + (V * 0.05)
        print ("Em 30 dias a renda vai ser:",NovoValor)
    else:
        print('Insira um tipo de investimento válido.')

def main():
    global investimento
    global valor
    investimento = int(input("Qual o tipo de investimento? "))
    valor = float(input("Qual o valor do depósito? "))
    Tipo_Investimento(investimento, valor)

if __name__ == '__main__':
    main()