#receber tipo de investimento com passagem de parâmetro



def Tipo_Investimento(I, V):
    NovoValor: float = 0.0
    if I == 1:
        NovoValor = V + (V * 0.03)
        return f"Em 30 dias a renda vai ser: {NovoValor}"
    elif I == 2:
        NovoValor = V + (V * 0.05)
        return f"Em 30 dias a renda vai ser: {NovoValor}"
    else:
        return 'Insira um tipo de investimento válido.'
    
def main():
    investimento: int = 0
    valor: float = 0.0
    NV: float = 0.0
    investimento = int(input("Qual o tipo de investimento? "))
    valor = float(input("Qual o valor do depósito? "))
    NV = Tipo_Investimento(investimento, valor)
    print (NV)



if __name__ == '__main__':
    main()
