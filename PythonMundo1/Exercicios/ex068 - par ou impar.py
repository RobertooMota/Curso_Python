import random

numeroCPU = 0
numeroUsuario = 0
placar = 0
par = 'PAR'
impar = 'IMPAR'
while True:
    numeroCPU = random.randint(1, 2)
    while True:
        escolhaUsuario = str(input('Escolhe [PAR] ou [IMPAR]? ')).upper()

        if escolhaUsuario == par or escolhaUsuario == impar:
            while True:
                numeroUsuario = int(input('Escolha um numero inteiro: '))
                if numeroUsuario >= 0:
                    break
            break
    resultado = numeroCPU + numeroUsuario
    if escolhaUsuario == par:
        if resultado % 2 == 0:
            print('Voce venceu!\n')
            placar += 1
        else:
            print('Voce Perdeu!!!\n')
            break
print(f'Total de vitorias consecutivas {placar}')
