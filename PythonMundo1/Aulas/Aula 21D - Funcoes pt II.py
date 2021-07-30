# Já nesse caso, quando o valor "a" for printado, ele será 20 pois existem duas variaveis chamadas "a" no programa
# uma local (dentro de teste2) e uma global

# =====================Ambiente Global===============================
# =====================Ambiente Local===============================
def teste2(value):
    a = 20
    print(a)
    print(a)
    b = 10
    print(b)
    c = 10
    print(c)


# =====================Ambiente Local===============================
a = 10
teste2(a)
# ===================================================================

# Para usar uma variavel global atribuindo um valor dentro de um ambiente local, basta usar a sintaxe:
#   global VARIAVEL