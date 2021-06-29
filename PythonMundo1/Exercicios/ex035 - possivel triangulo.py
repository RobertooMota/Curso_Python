retaA = int(input('Comprimento da reta A: '))
retaB = int(input('Comprimento da reta B: '))
retaC = int(input('Comprimento da reta C: '))

if retaB > retaC and retaB > retaA:
    if retaA + retaC > retaB:
        print('É possivel!')
    else:
        print('Não é possivel')
elif retaC > retaA and retaC > retaB:
    if retaA + retaB > retaC:
        print('É possivel!')
    else:
        print('Não é possivel!')
else:
    if retaB+retaC > retaA:
        print('É possivel!')
    else:
        print('Não é possivel!')
