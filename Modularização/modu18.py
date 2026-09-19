#Receba dois valores inteiros, calcule e mostre a diferença do menor pelo maior valor (SEM PASSAGEM DE PARAMETRO)

diferença: int = 0
num1: int = 0
num2: int = 0
maior: int = 0
menor: int = 0

def calc():
  if num1 > num2:
    maior = num1
    menor = num2
  else:
    maior = num2
    menor = num1
  diferença = maior - menor 
  print ('A diferença entre eles é:',diferença,)

def main():
  global num1 
  global num2
  num1 = int(input("Insira o primeiro número: "))
  num2 = int(input("Insira o segundo número: "))
  calc()

if __name__ == '__main__':
  main()