#Mostra se o numero digitado pelo usuario é primo

num = int(input('Digite um numero inteiro para o teste: '))
primo = bool(True)

for i in range(2, num):
    if num % i == 0:
        print('O numero digitado é divisivel por {}, resultado da divisão é: {}'.format(i, num/i))
        primo = False
if primo:
    print('O numero digitado é primo!')
else:
    print('O numero digitado não é primo!')
