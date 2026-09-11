#calcular hipotenusa

import math

cat1 = float(input("Qual o valor do primeiro cateto?: "))
cat2 = float(input("Qual o valor do segundo cateto?: "))
hipo = math.sqrt((cat1 * cat1) + (cat2 * cat2))
print("Esse e o valor da hipotenusa:",hipo)