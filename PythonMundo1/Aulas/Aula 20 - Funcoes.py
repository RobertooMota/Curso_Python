nota = []
nota.append(8)
nota.append(3)


def media(nota1, nota2):
    notafinal = (nota1 + nota2) / 2
    if notafinal >= 6:
        return 'aprovado'
    elif 5 <= notafinal < 6:
        return 'recuperação'
    else:
        return 'reprovado'


def linhas():
    print('-' * 20)


linhas()
print(f'{media(nota[1], nota[0]):>15}')
linhas()
