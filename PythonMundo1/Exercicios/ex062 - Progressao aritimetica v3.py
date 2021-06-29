#le o primeiro termo e a razao inseridos pelo usuario e mostra os 10 primeiros valores dessa PA

termo1 = int(input('Qual é o primeiro termo: '))
razao = int(input('Qual é a razão da P.A.: '))
PA = termo1
c = 10
while c != 0:
    PA = PA+razao
    print(PA)
    c -= 1

    if c == 0:
        res = str(input('Quer mostrar mais alguns termpos? [S/N]').upper())
        print(res)
        if res in 'sS':
            valor = int(input('Quantos termos a mais quer ver? '))
            c = c + valor