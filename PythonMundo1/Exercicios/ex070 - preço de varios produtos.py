totalGastos = 0
caros = 0
countCaros = 0
maisBaratoNome = ''
maisBaratoValor = 0


while True:
    produto = str(input('Nome do produto: '))
    valor = int(input('Preço do produto R$ '))
    if maisBaratoValor == 0:
        maisBaratoValor = valor
        maisBaratoNome = produto
        totalGastos += valor
    else:
        totalGastos += valor
        print(totalGastos)
        if valor > 1000:
            countCaros += 1
            caros += valor
    while True:
        resposta = str(input('Deseja continuar? [S/N]')).upper()
        if resposta not in 'SN':
            print('Informação incorreta!')
        else:
            break
    if resposta in 'nN':
        break

print(f'Valor total da compra R$: {totalGastos}')
print(f'Quantidade de produtos acima de R$ 1000 = {countCaros}', end='')
if countCaros > 0:
    print(f', totalizando o valor de R$ {caros}.')
else:
    print('.')
print(f'O produto mais barato foi: {maisBaratoNome}, custando R$ {maisBaratoValor}')


