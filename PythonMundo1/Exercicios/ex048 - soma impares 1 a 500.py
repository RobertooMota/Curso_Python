# Programa que soma todos os numeros que são impares e multiplos de 3 que estão entre o numero 1 e 500
somatoria = int(0)
for i in range(1, 500 + 1):
    if i % 2 == 1 and i % 3 == 0:
        somatoria += i
print('O valor é de: {}'.format(somatoria))
