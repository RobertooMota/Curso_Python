# Escobo de variáveis:
#   Uma variavel ela pode ser local ou global.
#   Para ser local, ela tem que ser declarada no ambiente RAIZ do desenvolvimento
#   Exemplo:

# =====================Ambiente Global===============================
# =====================Ambiente Local===============================
def teste(value):
    print(a)
    b = 10
    print(b)
    c = 10
    print(c)


# =====================Ambiente Local===============================
a = 10
teste(a)


# ===================================================================

# Nesse caso, dentro de teste, o 'a' é global então ao ser printado, o valor de print para "a" será 10


