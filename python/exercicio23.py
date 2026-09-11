#3 valores obrigatoriamente em ordem crescente e um 4, mostre os 4 em ordem crescente

N1 = int(input("Digite o 1o numero: "))
N2 = int(input("Digite o 2o numero: "))
N3 = int(input("Digite o 3o numero: "))
N4 = int(input("Digite o 4o numero: "))
if N4 < N1:
    print (N4,N1,N2,N3)
elif N4 < N2:
    print (N1,N4,N2,N3)
elif N4 < N3:
    print (N1,N2,N4,N3)
else:
    print (N1,N2,N3,N4)