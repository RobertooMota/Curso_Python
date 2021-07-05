from time import sleep

def separador():
    print('-=' * 30)


def contPadrao():
    a = 1
    b = 10
    passo = 1
    for i in range(a, b + 1):
        print(i, end=' ')
    print(' FIM!')
    separador()
    for i in range(b, a - 2, -2):
        print(i, end=' ')
    print(' FIM!')


def contador(inicio, fim, passo):
    for i in range(inicio, fim + passo, passo):
        print(i, end=' ')
        sleep(0.3)
    print(' FIM!')


separador()
contPadrao()
separador()

print('PERSONALIZADO')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
