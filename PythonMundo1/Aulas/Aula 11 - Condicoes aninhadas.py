#exemplo:
#Programa que dira se o numero digitado é maior, menor ou igual ao escolhido pelo programa
import random

value = int(input('Digite um valor entre 1 e 3, e veja se o advinha o que o programa escolheu! '))
valuePC = random.randint(1,3)

if value < 1 or value > 3:
    print('Valor incompativel! Inicie o programa novamente!')
elif value == valuePC:
    print('Voce acertou, o numero do PC éra o {}.'.format(valuePC))
elif value < valuePC:
    print('Voce errou, o valor escolhido pelo PC era {}!'.format(valuePC))
else:
    print('Voce errou, o valor escolhido pelo PC era {}!'.format(valuePC))
