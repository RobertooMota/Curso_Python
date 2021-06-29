#classifica atletas de acordo com a idade

idade = int(input('Idade do atleta: '))

if idade > 0  and idade <= 9:
    print('MIRIN')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <=19:
    print('JUNIOR')
elif idade > 19 and idade <= 25:
    print('SENIOR')
else:
    print('MASTER')
