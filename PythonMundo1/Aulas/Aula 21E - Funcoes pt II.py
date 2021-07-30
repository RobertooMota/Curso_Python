# Para usar uma variavel global atribuindo um valor dentro de um ambiente local, basta usar a sintaxe:
#   global VARIAVEL
# =====================Ambiente Global===============================
# =====================Ambiente Local===============================
def teste2(value):
    global a
    a = 20

    print(a)
    b = 10
    print(b)
    c = 10
    print(c)


# =====================Ambiente Local===============================
a = 10
print(f'variavel antes chamar a funcao {a}')
teste2(a)
print(f'variavel depois de chamar a funcao {a}')

# ===================================================================
