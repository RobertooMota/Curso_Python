#informa a quantidade de pessoas que ja sao de maiores e de menores
pessoa = []
deMaior = 0
deMenor = 0
anoAtual = 2021

for i in range(0, 7):
    pessoa.append(int(input('Digite o ano do seu nascimento: ')))

for i in range(0, 7):
    idade = int(anoAtual - pessoa[i])
    if idade >= 18:
        deMaior += 1
    else:
        deMenor += 1
print('Das pessoas listadas: {} são maior de idade e {} são menores de idade'.format(deMaior, deMenor))
