opcao = 4
while opcao == 4:
    numero1 = float(input('Digite um número '))
    numero2 = float(input('Agora, outro '))
    print('O que você quer fazer? ')
    print('[1] Soma')
    print('[2] Multiplicação')
    print('[3] Maior')
    print('[4] Escolher outros ')
    print('[5] Sair do programa')
    opcao = int(input('Faça a sua escolha: '))
    if opcao == 1:
        soma = float(numero1 + numero2)
        print('A soma é igual a {}'.format(soma))
    elif opcao == 2:
        print('O valor da multiplicação é igual a {}'.format(numero1 * numero2))
    elif numero1 > numero2 and opcao == 3:
        print('O maior valor é {}'.format(numero1))
    elif numero2 > numero1 and opcao == 3:
        print('O maior valor é {}'.format(numero2))
    elif opcao == 5:
        print('Então, tchau')
