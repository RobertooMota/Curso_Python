resposta = ''
aluno = list()
sala = list()

while True:
    aluno.append(input('Digite o nome do aluno: '))
    aluno.append(input(f'Digite nota da P1 do aluno {aluno[0]}: '))
    aluno.append(input(f'Digite nota da P2 do aluno {aluno[0]}: '))
    sala.append(aluno[:])
    aluno.clear()
    resposta = str(input('Deseja continuar? [S/N]'))
    if resposta.upper() not in 'S':
        break

print(sala)
# Nota da sala:
print('nº NOME         Média')
for i in range(0, len(sala)):
    print(f'{i+1}  {sala[i][0]}         {1:^4}')
