from datetime import datetime

cadastro = dict()
anoAtual = datetime.now().year


def separador():
    print('-=' * 10)


cadastro['Nome'] = str(input('Nome: '))
cadastro['Idade'] = anoAtual - (int(input('Ano de nascimento: ')))
cadastro['CTPS'] = int(input('Carteira de trabalho [0 = Não possui]: '))
if cadastro['CTPS'] != 0:
    cadastro['Ano de Contratacao'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = int(input('Salário: R$ '))
    cadastro['Idade aposentadoria'] = (anoAtual - cadastro['Ano de Contratacao']) + 35

separador()
for k, v in cadastro.items():
    print(f'{k}: {v}')
separador()
