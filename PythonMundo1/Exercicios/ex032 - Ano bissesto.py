ano = int(input('Qual ano quer saber? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano é bissesto!!')
else:
    print('O ano nao é bissesto!!')
