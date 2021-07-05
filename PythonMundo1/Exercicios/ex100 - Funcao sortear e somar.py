from random import randint

numeros = list()


def separador():
    print('~' * 50)


def sortear():
    for i in range(0, 6):
        numeros.append(randint(0, 10))
    return numeros


def somaPar(valores):
    soma = 0
    for i in valores:
        if i % 2 == 0:
            soma += i
    return soma


sorteados = sortear()
separador()
print(f'Valores sorteados foram {sorteados}')
print(f'Soma dos numeros pares dos valores sorteados: {somaPar(sorteados)}')
separador()