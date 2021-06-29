##   012345678901234
frase = '   Roberto Mota'
## [Inicio:Fim:intervalo]

# vai do slot 1 até o slot 6 do array
print(frase[1:6])

# vai do slot 1 até o slot 6 do array pulando de 3 em 3
print(frase[1:14:3])

# vai do slot INICIO até o slot FIM pulando de dois em dois
print(frase[::2])

# utilizando aspas triplas, ele printa respeitando a quebra de linha
print(""" Texto Texto Texto Texto Texto Texto 
 Texto Texto Texto Texto Texto Texto Texto Texto 
 Texto Texto Texto Texto Texto Texto Texto Texto 
 Texto Texto Texto Texto Texto Texto Texto """)

# .count ('caracter') = conta quantos caracteres daquele existe no alvo
print(frase.count('t'))

# faz o mesmo do anterior mas antes da contagem, deixa tudo maiusculo
print(frase.upper().count('t'))

# faz o mesmo do anterior mas antes da contagem, deixa tudo minusculo
print(frase.lower().count('t'))

# verifica o tamanho da frase
print(len(frase))

# .strip() remove os espacos antes ou depois da frase.
print(len(frase.strip()))

# .replace(oque sai, oque entra) simplesmente troca as palavras
# combinada com replace para remover os espacos do comeco e fim
# Replace nao altera a string efetivamente, somente no ponto de chamada.
print(frase.strip().replace('Mota', 'Moota'))

# para alterar a string usamos a atribuição
frase = frase.strip().replace('Mota', 'Mootaaaaaa')
print('Nova frase: {}'.format(frase))

print('Confirmacao de string alterada: {}'.format(frase))
frase = "Roberto Mota"

# procura alguma palavra ou um alvo em uma frase
# retornando verdadeiro ou falso
print('Mota' in frase)

# retorna a posicao do que estou procurando (caso exista)
print(frase.find('Mota'))  # Mota inicia na posicao 8

#.split cria uma lista da frase em questao
print(frase.split())
dividido = frase.split()
print(dividido[1])
