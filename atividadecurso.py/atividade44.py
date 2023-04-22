produto = float(input('Informe quanto custa o seu produto: '))
print('[1] Para pagar à vista no dinheiro /cheque')
print('[2] Para pagar à vista no cartão')
print('[3] Para pagar parcelando 2 vezes no cartão')
print('[4] Para pagar parcelando 3 vezes no cartão')
opcao = int(input('Escolha a opção de pagamento: '))
if opcao == 1:
    print('Você pagará {} reais pelo seu produto'.format(produto * 0.9))
elif opcao == 2:
     print('Você pagará {} reais pelo seu produto'.format(produto * 0.95))
elif opcao == 3:
     print('Você pagará {} reais pelo seu produto'.format(produto))
elif opcao == 4:
     print('Você pagará {} reais pelo seu produto'.format(produto * 1.2))
else:
    print('Você não selecionou nenhuma das opções de pagamento.')