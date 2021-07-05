# Nesse formato os parametros de entrada já são definidos em quantidade

def moldura(text):
    print('-' * 30)
    print(f'{text:^30}')
    print('-' * 30)


moldura(str(input('Seu texto: ')))


# Nesse formato, pode-se haver varias variaveis de entrada, e ela serão
# armazenadas em uma tupla que terá o nome do parametro de entrada
# nesse cado num.... ou seja.... num é uma tupla com a quantidade de parametros que forem passadas.
def numeros(*num):
    for i in range(len(num)):
        print(num[i])


numeros(1, 2, 3, 4, 5, 6, 6)
