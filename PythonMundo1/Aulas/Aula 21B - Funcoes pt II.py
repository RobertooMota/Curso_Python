# Parâmetros pré-definidos em funções:
# Nesse caso, caso a função seja chamada e não tenha o parâmetro B, automaticamente o B será um, pois o valor já está
# pré-definido
# Podemos tambem deixar todos os parametros já definidos, assim mesmo que não seja passado nada como parâmetro, ele
# não irá dar erro!

def exemploSoma(a=2, b=1):
    """
    -> Faz a somatória de dois parametros de entrada
    sendo ambos opcionais e por default valem:
    a = 2
    b = 1
    e retornar o valor da soma
    """
    return a + b


print(f'Print somente com um parâmetro... a = 10: {exemploSoma(10)}')
print(f'Print com dois parâmetro... a = 10 e b = 20: {exemploSoma(10, 20)}')
print(f'Print sem parâmetro...:{exemploSoma()}')
