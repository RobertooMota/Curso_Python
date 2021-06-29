# le um numero e mostra o fibonacci ate ele

numUsuario = int(input('Digite um numero inteiro: '))

aux = 1
anterior = 0
atual = 0
count = 0

while count < numUsuario:
    # 0 -- 1 -- 1 -- 2 -- 3
    if count  == numUsuario - 1:
        print(atual, end='')
        count += 1
    else:
        print(atual, ' ~~> ', end='')
        anterior = aux
        aux = atual
        atual = atual + anterior
        count += 1
print(' [FIM]')
