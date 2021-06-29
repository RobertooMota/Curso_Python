import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))
print(hipotenusa)
