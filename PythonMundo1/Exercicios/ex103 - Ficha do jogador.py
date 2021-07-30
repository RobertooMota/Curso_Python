def ficha(jogador='<DESCONHECIDO>', gols=0):
    print('~' * 30)
    print(f'O jogador {jogador} marcou {gols} gol(s)!')
    print('~' * 30)


nomeJogador = str(input('Nome do jogador: '))
try:
    golsJogador = int(input('Gol(s) marcado(s): '))
except:
    golsJogador = 0

if nomeJogador == '':
    ficha(gols=golsJogador)
else:
    ficha(jogador=nomeJogador, gols=golsJogador)
