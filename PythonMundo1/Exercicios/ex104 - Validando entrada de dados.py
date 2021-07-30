def leiaInt(text):
    while True:
        entrada = str(input(text))
        if entrada.isnumeric():
            return entrada
        else:
            print(f'\033[0;31mERRO!!! {entrada} não é um número!!!\033[m')


# Programa principal

n = leiaInt('Digite um número: ')
print(f"Você acabou de digitar o número {n}!\nFIM!!!")

