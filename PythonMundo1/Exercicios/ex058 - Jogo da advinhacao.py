#Escolhe um numero randomico entre 0 e 10 e pede pro usuario advinhar
import random
escolhaPC = random.randint(0, 10)
print(escolhaPC)
escolhaUsuario = int(input('Escolha um valor de 0 a 10: '))
palpites = int(1)

if 0 <= escolhaUsuario <= 10:
    while escolhaUsuario != escolhaPC:
        palpites = palpites + 1
        escolhaUsuario = int(input('Valor errado! Tente novamente: '))
    if escolhaUsuario == escolhaPC:
        print('Parabens voce acertou! Foram necessários {} palpites'.format(palpites))
else:
    print('valor invalildo!!!')


