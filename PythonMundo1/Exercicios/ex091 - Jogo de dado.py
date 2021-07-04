from operator import itemgetter
from random import randint
from time import sleep


def linhas():
    print('-' * 20)


jogadores = {
    'Jogador 1': randint(0, 6),
    'Jogador 2': randint(0, 6),
    'Jogador 3': randint(0, 6),
    'Jogador 4': randint(0, 6)
}
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')

linhas()
print('Ordem de vencedores!')
linhas()

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}° Lugar: {v[0]} com {v[1]}')
