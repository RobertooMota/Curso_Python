frase = str(input('Digite uma frase para o teste: ')).upper().strip()
frase = frase.split()
letras = ''.join(frase)
inverso = ''
#invertendo
for i in range(len(letras)-1, -1, -1):
    inverso += letras[i]
print(inverso)

if letras == inverso:
    print('É palindromo!')
else:
    print('Não é palindromo!')