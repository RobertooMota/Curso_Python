mat = str(input('Digite sua expressão matemática: '))
paren = 0
for item in mat:
    if item == '(':
        paren += 1
    elif item == ')':
        paren -= 1
if paren == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
