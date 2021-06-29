#analisa as notas das provas e identifica se PASSOU, REPROVOU ou ficou de RECUPERACAO
nota1 = float(input('Nota prova 1: '))
nota2 = float(input('Nota prova 2: '))
media = (nota1 + nota2) / 2

if media < 5 and media >= 0:
    print('Reprovado!')
elif media >= 7 and media <= 10:
    print('Aprovado!')
elif media >= 5 and media < 7:
    print('Recuperacão!')
else:
    print('Confira os valores das notas!!! pois o resultado da media não está entre 0 e 10!')