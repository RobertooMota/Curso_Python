def notas(*value, situacao=False):
    aluno = dict()
    aluno['total'] = len(value)
    aluno['maior nota'] = max(value)
    aluno['menor nota'] = min(value)
    aluno['media'] = sum(value) / len(value)
    if not situacao:
        print(
            f'Total: {aluno["total"]}   Maior nota: {aluno["maior nota"]}   Menor nota: {aluno["menor nota"]}   '
            f'Média: {aluno["media"]:.2f}')
    else:
        if aluno['media'] >= 6:
            aluno[situacao] = 'aprovado'
        else:
            aluno[situacao] = 'reprovado'
        print(
            f'Total: {aluno["total"]}   Maior nota: {aluno["maior nota"]}   Menor nota: {aluno["menor nota"]}   '
            f'Média: {aluno["media"]:.2f}  Situação: {aluno[situacao]}')


notas(7, 5, 6, situacao=True)
