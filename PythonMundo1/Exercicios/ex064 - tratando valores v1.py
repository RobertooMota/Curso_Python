valor = 0
somatorio = 0
count = 0
while valor != 999:
    valor = int(input('Digite um valor, se digitar 999 o programa irá parar! '))

    if valor == 999:
        print('\nFlag detectada!\nFim do programa!\n')
    else:
        somatorio += valor
        count += 1
print('Foram digitados {} valores e a soma deles é de: {}'.format(count, somatorio))
