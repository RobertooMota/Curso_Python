def metade(valor, um='R$'):
    resultado = valor / 2
    return f'A metade de {um}{valor:.2f} é de {um} {resultado:.2f}'.replace('.', ',')


def dobro(valor, um='R$'):
    resultado = valor * 2
    return f'O dobro de {um}{valor:.2f} é de {um} {resultado:.2f}'.replace('.', ',')


def aumentado(valor, um='R$'):
    resultado = valor * 1.10
    return f'O valor aumentado em 10% de {um}{valor:.2f} é de {um} {resultado:.2f}'.replace('.', ',')
