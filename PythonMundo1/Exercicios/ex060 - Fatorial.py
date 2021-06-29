#le o valor do usuario e faz o fatorial

num = int(input('Digite um valor para o fatorial: '))
escolhaUsuario = num
resultado = 1
if num > 0:
    while num > 0:
        resultado = resultado * num
        if num > 1:
            print(num, ' x ', end='')
        else:
            print(num, '= ', end='')
        num -= 1

print('Resultado da fatorial de {} é igual a: {}'.format(escolhaUsuario, resultado))
