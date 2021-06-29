# listas parte 1

# criar lista
minhaLista = list(range(0, 5))
print(
    f'\nTamanho da Lista ao ser declarada: {len(minhaLista)}')  # Ao printar, comprimento da lista sera de 5 unidades ou slots

# Atribuir um valor a um slot da lista

minhaLista[0] = 'Amarelo'
print(f'Apos tribuir um valor a lista: {minhaLista[0]}')

# Quando determinamos o tamanho da lista na sua declaração, armazena somente aquele tanto de informação.
# Mas caso queiramos adicionar mais slots, usamos os comandos .insert(posicao, Variavel) ou .append(variavel)

minhaLista.append('azul')
print(f'\nVariavel AZUL adicionado a posição {minhaLista.index("azul")} da lista! ')

minhaLista.insert(2, 'Melancia')
print(f'\nAdicionando um elemento em um local especifico: Local 2 item: {minhaLista[2]}')

# Formas de deletar um item da lista.
print(f'\nLista Atual: {minhaLista}')
del minhaLista[0]  # nesse caso ele deleta o item do slot e reorganiza toda a lista
print(f'Posicao 0 da lista onde havia o valor "amarelo" apos comando del minhalista[0]')
print(minhaLista)

print('\nApos usar o comando .pop() : ')
minhaLista.pop()  # deleta o ultimo item da lista ou pode ter um target .pop(local)
print(minhaLista)

print('\nApos usar o comando remove("Melancia"): ')
minhaLista.remove('Melancia')
print(minhaLista)

print('\n\n\n')
print('-' * 30)
print('Lista com valores numericos')
print('-' * 30)

print('Lista com valores aleatorios:', end='')
numeros = [3, 10, 2, 9, 13, 2, 6, 7, 8]

print('\nLista com comando .sort para organizar:', end='')
numeros.sort()
print(numeros)

print('\n lista com ordem reversa com comando reverse como parametro em sort: ', end='')
numeros.sort(reverse=True)
print(numeros)

