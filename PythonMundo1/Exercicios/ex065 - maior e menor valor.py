# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.

ciclos = int(input('Quantos numeros quer digitar? '))
count = 0
numeros = 0
soma = 0
maior = 0
menor = 0
media = 0
x = 0
while count < ciclos:
    numeros = int(input('Digite um valor: '))
    soma += numeros
    count += 1
    if numeros > maior:
        maior = numeros
    if menor == 0:
        menor = numeros
    elif numeros < menor:
        menor = numeros

    if count == ciclos:
        resposta = str(input('Quer continuar? '))
        if resposta in 'sS':
            ciclos = ciclos + int(input('Quantos ciclos quer acrescentar? '))
# media
print('Maior {} \nMenor {} \nMédia {}\n'.format(maior, menor, soma / ciclos))

