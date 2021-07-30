def anoAtual():
    from datetime import date
    return date.today().year


def voto(valor):
    idade = anoAtual() - valor
    if idade > 0:
        if idade >= 18:
            return f'Com {idade} anos de idade, é obrigatório o voto!'
        elif idade >= 16 and idade < 18:
            return f'Com {idade} anos de idade, o voto é opcional!'
        else:
            return f'Com {idade} anos de idade, não é permitido o voto!'
    else:
        return 'Confira a data inserida!'


print(voto((int(input('Digite seu ano de nascimento: ')))))
