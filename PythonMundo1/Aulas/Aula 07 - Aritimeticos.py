n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

# Quando se usa {: nValor } é uma declaração de espacamento no local onde está especificado.
# Quando se usa {:.nValor f } é uma declaração de quantos numeros depois da virgula queremos que seja exibido
#   por isso usamos um 'f' no final (FLUTUANTE).

#end=""   <---- declara o que acontecerá no final da linha. Nesse caso não irá pular a linha (o que acontecia
#   anteriormente devido a termos dois prints separados.
print('Divisao: {:.4f} Multiplicacao: {} Exponenciacao: {}'.format((n1 / n2), (n1 * n2), (n1 ** n2)), end="")
print('Fim de calculos!')

