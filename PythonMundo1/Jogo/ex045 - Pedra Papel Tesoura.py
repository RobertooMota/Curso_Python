# jogo pedra papel tesoura
import random

escolhaHumano = str(input('Escolha entre -----)>  PAPEL | PEDRA | TESOURA | =====>>>  ').lower())
escolhaMachine = ['pedra', 'papel', 'tesoura']

escolhaAtual = random.randint(0, 2)
print('\n')
print('Machine      você')
print(escolhaMachine[escolhaAtual] + ' ---> ' + escolhaHumano)


if escolhaMachine[escolhaAtual] == 'pedra':
    if escolhaHumano == 'pedra':
        print('Empate!')
    elif escolhaHumano == 'tesoura':
        print('Voce perdeu!!! BLAAAAAAAAAAAAAAAA')
    else:
        print('Voce ganhou... :@ ')

elif escolhaMachine[escolhaAtual] == 'tesoura':
    if escolhaHumano == 'pedra':
        print('Voce ganhou... :@ ')
    elif escolhaHumano == 'tesoura':
        print('Empate!')
    else:
        print('Voce perdeu!!! BLAAAAAAAAAAAAAAAA')

else:
    if escolhaHumano == 'pedra':
        print('Voce perdeu!!! BLAAAAAAAAAAAAAAAA')
    elif escolhaHumano == 'tesoura':
        print('Voce ganhou... :@ ')
    else:
        print('Empate!')
