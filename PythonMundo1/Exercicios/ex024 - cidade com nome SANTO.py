nome = input('Digite o nome da sua cidade: ').strip()
testeLogico = 'SANTO'
splitado = nome.upper().split()

print(testeLogico in splitado[0])
