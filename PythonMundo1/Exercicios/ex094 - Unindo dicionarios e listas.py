pessoa = dict()
listaPessoas = list()
somaIdade = 0
mediaIdade = 0

temMulher = bool(0)
acimaMedia = bool(0)


def separador():
    print('-' * 20)


while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]'))
    pessoa['Idade'] = int(input('Idade: '))
    listaPessoas.append(pessoa.copy())
    pessoa.clear()

    if str(input('Deseja continuar? [S/N]: ')) not in 'sS':
        break

separador()
# Pessoas cadastradas
print(f'Foram cadastradas {len(listaPessoas)} pessoas.')
separador()

# Média de idade
for i in range(0, len(listaPessoas)):
    somaIdade += listaPessoas[i]['Idade']
mediaIdade = somaIdade / len(listaPessoas)
print(f'A média de idade é de: {mediaIdade:.1f} anos.')

separador()
# Lista com mulheres
for i in range(0, len(listaPessoas)):
    if listaPessoas[i]['Sexo'] in 'fF':
        temMulher = True
if temMulher:
    print('Mulheres cadastradas: ', end='')
    for i in range(0, len(listaPessoas)):
        if listaPessoas[i]['Sexo'] in 'fF':
            print(f'{listaPessoas[i]["Nome"]}', end=' ')
else:
    print('Não há mulheres cadastradas!')
print('')
separador()

# Pessoas acima da média de idade
for i in range(0, len(listaPessoas)):
    if listaPessoas[i]['Idade'] > mediaIdade:
        acimaMedia = True
        break
if acimaMedia:
    print('Pessoas com a idade acima da média: ')
    for i in range(0, len(listaPessoas)):
        if listaPessoas[i]['Idade'] > mediaIdade:
            print(
                f'Nome: {listaPessoas[i]["Nome"]}, Sexo: {listaPessoas[i]["Sexo"]}, Idade: {listaPessoas[i]["Idade"]}.')
else:
    print('Não há pessoas com a idade acima da média!')
