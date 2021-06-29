valores = []
count = 0
while True:
    valores.append(int(input('Digite um valor: ')))

    resposta = str(input('Deseja continuar? [S/N]'))
    if resposta in 'nN':
        break

# Quantidade de numeros
print(f'Foram digitados {len(valores)} numeros!')

# valores em ordem decrescente
valores.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foram = {valores}!')

# foi digitado valor 5? se sim, quantos?
####################################Solucao minha########################
for i in valores:
    print(f'for para buscar o 5 {i}')
    if i == 5:
        valor_5 = True
print(f'---Minha solucao---')
if valor_5 == True:
    print('Valor 5 foi digitado!')
else:
    print('Valor 5 não foi digitado!')

##############################solucao do professor########################
print(f'---Solucao do provessor---')
if 5 in valores:
    print('Valor 5 foi digitado!')
else:
    print('Valor 5 não foi digitado!')
