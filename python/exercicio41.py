#dois dados com possibilidade de soma 7 

D1: int = 1
while D1 <= 6:
    D2: int = 1
    while D2 <= 6:
        if D1 + D2 == 7:
            print (D1,D2)
        D2 = D2 + 1
    D1 = D1 + 1    

