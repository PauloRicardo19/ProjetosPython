#preço novo de um produto com alguns reajustes com passagem de parâmetros



def Alterações_Valores(PA, V):
    PN: float = 0.0
    if V < 500 and PA < 30:
        PN = PA + (PA * 0.10)
    elif V >= 500 and V <1000 and PA >= 30 and PA <80:
        PN = PA + (PA * 0.15)
    elif V >= 1000 and PA >= 80:
        PN = PA - (PA * 0.05)
    else:
        PN = PA
    return PN

def main():
    PreçoAtual: float = 0.0
    Venda: float = 0.0
    PreçoAtual = float(input("Qual o preço atual do produto? "))
    Venda = float(input("Quantos produtos são vendidos mensalmente? "))
    Alterações_Valores(PreçoAtual, Venda)
    PN = Alterações_Valores(PreçoAtual, Venda)
    print ('Esse é o novo valor',PN)

if __name__ == '__main__':
    main()
