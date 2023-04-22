num = int(input('Escreva qual número você quer converter: '))
print('[1] Para converter para binário.')
print('[2] Para converter para octal.')
print('[3] Para converter para hexadecimal.')
opcao = int(input('Escolha um dos números acima: '))
if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
     print('{} convertido para binário é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
     print('{} convertido para binário é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Desculpe, mas você não escolheu nenhumas das opções disponíveis.')