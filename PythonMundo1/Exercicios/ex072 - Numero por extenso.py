numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco')

numUsuario = int(input('Digite um numero de 0 a 5: '))

while True:
    if 0 <= numUsuario <= 5:
        print(f'Você digitou o numero {numeros[numUsuario]}')
        resposta = str(input('Continuar? [S/N]'))
        if resposta in 'sS':
            numUsuario = int(input('Digite um numero de 0 a 5: '))
        else:
            break
    else:
        numUsuario = int(input('Valor invalido: Digite um numero de 0 a 5: '))
