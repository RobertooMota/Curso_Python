# Fatorial

def fatorial(value):
    resultado = 1
    for i in range(value, 0, -1):
        resultado *= i
    return resultado


print(f'Resultado da fatorial: {fatorial(int(input("Digite um numero inteiro: ")))}')
