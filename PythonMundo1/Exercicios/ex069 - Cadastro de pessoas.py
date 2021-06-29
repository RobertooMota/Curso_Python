maiores = 0
homens = 0
mulheres = 0
while True:
    print('-----------------')
    print('   Cadastrar')
    print('-----------------')
    while True:
        idade = int(input('Digite a idade: '))
        if idade == 0:
            print('Valor não aceito, tente um valor maior que "0"')
        else:
            break
    while True:
        sexo = str(input('Informe o sexo: [M/F]'))
        if sexo not in 'mMfF':
            print('Informação digitada incorreta. Tente [M] para masculino ou [F] para feminino!')
        else:
            break

    if idade >= 18:
        maiores += 1

    if sexo in 'mM':
        homens += 1

    if sexo in 'fF':
        if idade < 20:
            mulheres += 1
    while True:
        continuar = str(input('Deseja continuar? '))
        if continuar not in 'sSnN':
            print('informacao incorreta! Tente novamente.')
        else:
            break
    if continuar in 'nN':
        break

print(f'{maiores} pessoas tem menos de 18 anos.\n{homens} homens foram cadastrados.\n{mulheres} mulheres tem mais de 20 anos de idade.')
