times = ('América Mineiro', 'Belo Horizonte', 'Minas Gerais MG', 'Independência', 'Athletico Paranaense', 'Curitiba',
         'Paraná PR', 'Arena da Baixada', 'Atlético', 'Goianiense', 'Goiânia', 'Atlético Mineiro', 'Chapecó',
         'Corinthians', 'São Paulo')

print('Os cinco primeiros colocados são:')
for i in range(0,5):
    print(f'{i+1}º {times[i]}')
print('\nOs ultimos quatro colocados são:')
for i in range(len(times) - 4, len(times)):
    print(f'{i+1}° {times[i]}')
timesEmOrdem = sorted(times)


print(f'\nO time curitiba se encontra na posiçã {times.index("Curitiba")+1} da tabela')

print('\nTimes em ordem alfabetica:\n =========================')
for timeAtual in timesEmOrdem:
    print(timeAtual)
