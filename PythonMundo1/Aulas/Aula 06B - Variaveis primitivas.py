#Teste com tipo bool
#como o valor bool só pode ser verdadeiro ou falso, se houver algum valor armazenado em "value" ele retornara verdadeiro
value = bool(input('Digite um valor: '))
print('Status do valor digitado: {}'.format(value))

value_2 = input('Digite algo: ')
print(value_2.isnumeric())

