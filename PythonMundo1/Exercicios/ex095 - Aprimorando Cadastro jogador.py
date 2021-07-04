todosJogadores = list()
cadastro = dict()
gols = list()


def separador():
    print('-' * 50)


while True:
    cadastro['Nome'] = str(input('Nome: '))
    totalPartidas = int(input('Quantas partidas jogou? '))
    for i in range(0, totalPartidas):
        gols.append(int(input(f'Gols da partida {i + 1}: ')))
    cadastro['Gols'] = gols[:]
    cadastro['Total'] = sum(gols)
    todosJogadores.append(cadastro.copy())
    gols.clear()
    print(cadastro)
    if str(input('Deseja continuar [S/N]? ')) not in 'sS':
        break


separador()
print(f'{"COD":<5}{"Nome":<20}{"Gols":<15}{"Total":>5}')
separador()

for i, v in enumerate(todosJogadores):
    print(f'{i:<5}{v["Nome"]:<20}{str(v["Gols"]):<15}{str(v["Total"]):>5}')
