# value = bool(input('Digite 1 ou 0: '))
# if value == 0:
#    print('Verdadeiro')
# else:
#    print('false')
n1 = float(input('Valor da primeira nota: '))
n2 = float(input('Valor da segunda nota: '))
media = (n1 + n2) / 2
print('Sua média foi: {:.1f}'.format(media))
if media >= 6:
    print('Aprovado!')
else:
    print('Reprovado!!!')

print('---------------------- IF SIMPLIFICADO ----------------------')
print('Aprovado!' if media >= 6 else 'Reprovado!!!')
