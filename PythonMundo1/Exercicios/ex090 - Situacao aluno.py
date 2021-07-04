aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = int(input(f'Media do aluno {aluno["nome"]}: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')