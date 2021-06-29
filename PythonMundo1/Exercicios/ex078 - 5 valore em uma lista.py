valores = []

for i in range(0, 5):
    valores.append(int(input(f'Digite o {i + 1}° valor: ')))

print(f'\nMaior valor digitado: {max(valores)} na(s) posição(ões): ', end='')
for i in range(0, len(valores)):
    if valores[i] == max(valores):
        print(f'..{i}', end='')
print('')

print(f'Menor valor digitado: {min(valores)} na(s) posição(ões): ', end='')
for i in range(0, len(valores)):
    if valores[i] == min(valores):
        print(f'..{i}', end='')

print('\n\nPosição de cada item da lista e seu valor:')
for pos, i in enumerate(valores):
    print(f'Posição: {pos}... Valor: {i}')
