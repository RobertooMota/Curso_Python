import random
value = random.randint(0, 5)
valueUser = int(input('Qual valor acha que foi escolhido: '))
if valueUser == value:
    print('Você acertou!!!')
else:
    print('Voce errou! O valor escolhido era: {}'.format(value))

print('Obrigado por jogar!')

