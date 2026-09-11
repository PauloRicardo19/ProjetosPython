#diferença entre dois valores
diferença: int = 0
num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))
if num1 > num2:
    diferença = num1 - num2
    print ("A diferença e de:",diferença)
else:
    diferença = num2 - num1
    print ("A diferença e de:",diferença)