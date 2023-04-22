import random
lista = [1, 2, 3]
opcao_computador = random.choice(lista)
print('[1] para pedra')
print('[2] para papel')
print('[3] para tesoura')
opcao = int(input('Faça a sua escolha '))
if (opcao_computador == 1 and opcao == 3) or (opcao_computador == 2 and opcao == 1) or (opcao_computador == 3 and opcao == 2):
    print('O computador escolheu {}, você perdeu'.format(opcao_computador))
elif (opcao_computador == 3 and opcao == 1) or (opcao_computador == 1 and opcao == 2) or (opcao_computador == 2 and opcao == 3):
    print('O computador escolheu {}, você ganhou'.format(opcao_computador))
elif opcao != 1 or opcao != 2 or opcao != 3:
    print('Escolha alguma das opções que eu te mostrei!')
