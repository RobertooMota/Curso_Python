# Le os pesos de 5 pessoas e diz o maior e o menor
pessoa = []
maiorPeso = 0
menorPeso = 0
menor = int(0)

for i in range(0, 5):
    pessoa.append(float(input('Digite o pesso da pessoa {}: '.format(i + 1))))

for i in range(0, 5):
    for n in range(0, 5):
        if pessoa[i] > pessoa[n]:
            maior = i

        if pessoa[i] < pessoa[n] and pessoa[i] < pessoa[menor]:
            menor = i

print('O maior peso foi da pessoa numero {} (peso: {}kg) e o menor foi da pessoa numero {} (peso {}kg)!'.format(maior + 1,pessoa[maior] , menor + 1,pessoa[menor] ))
