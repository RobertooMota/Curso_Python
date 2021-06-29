
nome = []
sexo = []
idade = []
maisVelho = int
maisNovas = int
idadeAnterior = int

for i in range(0, 4):
    nome.append(str(input('Nome {}: '.format( i +1))))
    sexo.append(str(input('Sexo (M) ou (F): ').upper()))
    idade.append(int(input('Idade: ')))

for i in range(0, 4):
    print('Nome: {}  Idade: {} anos   sexo: {} '.format(nome[i], idade[i], sexo[i]))

# media de idade
media = int(0)
for i in range(0, 4):
    media = media + idade[i]
media = media / 4
print('Media de idade = {} '.format(media))

# homem mais velho
idadeAnterior = 0
maisVelho = 0

for i in range(0, 4):
    if sexo[i] == 'M':
        if idade[i] > idadeAnterior:
            maisVelho = i
            idadeAnterior = idade[i]

print('O homem mais velho é o {}'.format(nome[maisVelho]))

# Mulheres mais novas do que 20 anos
maisNovas = 0
for i in range(0, 4):
    if sexo[i] == 'F':
        if idade[i] < 20:
            maisNovas = maisNovas + 1
if maisNovas > 0:
    print('Dessa lista, {} mulheres tem menos que 20 anos de idade!' .format(maisNovas))
else:
    print('Dessa lista todas tem mais que 20 anos de idade!')
