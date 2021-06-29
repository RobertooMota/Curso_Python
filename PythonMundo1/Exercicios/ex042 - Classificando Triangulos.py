retaA = int(input('Comprimento da reta A: '))
retaB = int(input('Comprimento da reta B: '))
retaC = int(input('Comprimento da reta C: '))
classificacao = int(0)

if retaB > retaC and retaB > retaA:
    if retaA + retaC > retaB:
        print('É possivel!')
        classificacao = 1
    else:
        print('Não é possivel')
elif retaC > retaA and retaC > retaB:
    if retaA + retaB > retaC:
        print('É possivel!')
        classificacao = 1
    else:
        print('Não é possivel!')
else:
    if retaB + retaC > retaA:
        print('É possivel!')
        classificacao = 1
    else:
        print('Não é possivel!')

if classificacao == 1:
    if retaA == retaB and retaB == retaC:
        print('O triangulo é do tipo equilatero!')  # Todos os lados iguais
    elif retaA != retaB and retaB != retaC and retaC != retaA:
        print('O triangulo é do tipo escaleno!')  # Todos lados diferentes
    else:
        print('O triango é do tipo isosceles!')  # dois lados iguais
