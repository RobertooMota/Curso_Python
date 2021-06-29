# pega valores digitado pelo usuario, se for par soma todos e mostra os impares. se for impar ele desconsidera.
valor = []
soma = int(0)
for num in range(0, 6):
    valor.append(int(input('Digite o {}° valor: '.format(num+1))))

for i in range(0, 6):
    soma = soma + valor[i]

if soma % 2 != 0:
    print('A soma dos 6 valores inseridos resulta em um numero IMPAR!')
else:
    for i in range(0, soma+1):
        if i % 2 == 0:
            print('valores pares: {}'.format(i))
