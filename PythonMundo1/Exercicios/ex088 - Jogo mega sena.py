import random

jogos = list()
palpite = list()

while True:
    numJogos = int(input('Quantos jogos deseja fazer? '))
    for i in range(0, numJogos):
        for x in range(0, 6):
            palpite.append(random.randint(0, 60))
        jogos.append(palpite[:])
        palpite.clear()
    break
print(f'Foram gerados {numJogos} jogos!')
for pos, i in enumerate(jogos):
    print(f'Jogo número {pos + 1}: {i} ')
