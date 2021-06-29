# Le dois valores e apresenta um menu com as operacoes possiveis
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('')

menu = ['[1] - somar', '[2] - Multiplicar', '[3] - Maior', '[4] - Novos numeros', '[5] - Sair do programa!']
menuOpen = True
opcaoUsuario = 0
# -------------------Abre o menu----------------
while menuOpen:
    if n1 != 0 and n2 != 0:
        for i in range(0, 5):
            print(menu[i])
        opcaoUsuario = int(input('\nQual é sua opção? '))
        # -------------Avalia a opcao do usuario----------
        if 0 < opcaoUsuario <= 5:
            if opcaoUsuario == 1:
                print('{} = {}'.format(menu[opcaoUsuario - 1], n1+n2))
                print('')
            elif opcaoUsuario == 2:
                print('{} = {}'.format(menu[opcaoUsuario - 1], n1 * n2))
                print('')
            elif opcaoUsuario == 3:
                if n1 > n2:
                    print('{} = {}'.format(menu[opcaoUsuario - 1], n1))
                    print('')
                else:
                    print('{} = {}'.format(menu[opcaoUsuario - 1], n2))
                    print('')
            elif opcaoUsuario == 4:
                print(menu[opcaoUsuario - 1])
                n1 = int(input('Digite o primeiro valor: '))
                n2 = int(input('Digite o segundo valor: '))
                print('')
            else:
                menuOpen = False
        else:
            print('\n\nOpcao Incorreta!\nEscolha Novamente!\n\n')
    else:
        print('Dois valores ZERO não é permitido!\n\n')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
