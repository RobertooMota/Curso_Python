jogador = dict()

jogador['Nome'] = str(input('Nome: '))
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
gols = 0


def separador():
    print('#' * 30)


for i in range(0, jogador['Partidas']):
    jogador[f'Partida {i + 1}'] = int(input(f'Quantos gols marcados na partida {i + 1}: '))
    gols = gols + jogador[f'Partida {i + 1}']
print('')
separador()
for k, v in jogador.items():
    if k == 'Nome':
        print(f'Nome do jogador: {v.capitalize()}')
    elif k == 'Partidas':
        print(f'Jogou {v} partidas.')
    else:
        print(f'Na {k} Marcou {v} gols.')
print(f'Foi um total de {gols} gols.')
separador()
