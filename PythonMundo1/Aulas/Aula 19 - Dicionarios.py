filme = {
    'nome': 'StarWars',
    'ano': 1977,
    'nota': 8
}
locadora = []

print(filme)
for k, v in filme.items():  #Similar ao enumerate
    print(f'O {k} é {v}')

locadora.append(filme)
print(locadora)

