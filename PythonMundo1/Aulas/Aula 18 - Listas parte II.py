dados = ['Joao', 34]
dadoss = ['Maria', 23]
dados2 = list()
dados2.append(dados[:])
print(dados2[0])
dados2.append(dadoss[:])
print(dados2[1])
print(dados2)

print('\nTeste 2\n')
pessoas = [['Joao', 13], ['Maria', 23], ['Fagner', 12]]
for item in pessoas:
    print(item)
print(pessoas)

print('teste 3 \n\n')

galera = list()
pessoa = ['Joao', 23]
galera.append(pessoa[:])
pessoa[0] = 'Maria'
pessoa[1] = 33
galera.append(pessoa[:])

print('Galera: ')
print(galera)