#confere a idade e direciona de acordo para alistamento.

anoNascimento = int(input('Ano de nascimento: '))
anoAtual = int(2021)
idadeAlistamento = (18)
idadeAtual = anoAtual - anoNascimento

if idadeAtual < idadeAlistamento:
    print('Ainda não é o momento do alistamento, ainda falta {} anos!'.format(idadeAlistamento - idadeAtual))
elif idadeAtual > idadeAlistamento:
    print('Passou do tempo do alistamento em {} ano(s)!!!!'.format(idadeAtual - idadeAlistamento))
else:
    prin('Essa é a hora exata para o alistamento!')
