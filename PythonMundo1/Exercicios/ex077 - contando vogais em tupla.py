palavras = ('ola', 'martelo', 'pipoca', 'carro', 'trabalho', 'maquina', 'arara')
A = E = I = O = U = 0
for teste in palavras:
    print(f'Na palavra {teste} temos as vogais: ', end='')
    for testeIndividual in teste:
        if testeIndividual.lower() in 'aeiou':
            print(testeIndividual, end=' ')
    print('')

