# Exercicio 54 utilizando biblioteca para ter o ano atual

from datetime import date

atual = date.today().year
maiorIdade = 0
menorIdade = 0
pessoa = []
for i in range(0, 7):
    pessoa.append(int(input('Idade da {}º pessoa: '.format(i + 1))))

for i in range(0, 7):
    if pessoa[i] >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1

print('Quantidade de pessoas maiores de idade: {} pessoas!'.format(maiorIdade))
print('Quantidade de pessoas menores de idade: {} pessoas!'.format(menorIdade))
