resposta = ''
aluno = list()
sala = list()

while True:
    aluno.append(input('Digite o nome do aluno: '))
    aluno.append(int(input(f'Digite nota da P1 do aluno {aluno[0]}: ')))
    aluno.append(int(input(f'Digite nota da P2 do aluno {aluno[0]}: ')))
    sala.append(aluno[:])
    aluno.clear()
    resposta = str(input('Deseja continuar? [S/N]'))
    if resposta.upper() not in 'S':
        break

print(sala)
# Nota da sala:
print(f'{"No°":<4}{"Nome":<10}{"Média":>8}')
for i in range(0, len(sala)):
    print(f'{i+1:<4}{sala[i][0]:<10}{(sala[i][1] + sala[i][2]) / 2:>8.1f}')

while True:
    individual = int(input('Digite qual aluno deseja saber a nota: '))
    if individual == 999:
        break
    else:
        print(f'Notas do {sala[individual - 1][0]}: {sala[individual - 1][1:]}')
