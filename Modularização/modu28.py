#preço novo de um produto com alguns reajustes com passagem de parâmetros

PreçoAtual: float = 0.0
Venda: float = 0.0

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
    print ('Esse é o Novo Preço:',PN)

def main():
    global PreçoAtual
    global Venda
    PreçoAtual = float(input("Qual o preço atual do produto? "))
    Venda = float(input("Quantos produtos são vendidos mensalmente? "))
    Alterações_Valores(PreçoAtual, Venda)

if __name__ == '__main__':
    main()
