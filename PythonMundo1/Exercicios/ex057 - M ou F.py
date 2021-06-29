#pede para o usuario digita o sexo dele F ou M. se for digitado algo fora desse contexto, pergunta novamente.

sexo = input('Digite o seu sexo: M / F  ').upper()
while sexo not in 'mMfF':
    sexo = input('Informacao incorreta. Por favor, insira: M / F  ').upper()

if sexo == 'F':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'
print('O sexo informado foi {}.'.format(sexo))
