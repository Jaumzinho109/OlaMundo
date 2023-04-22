maioridade = 0
menoridade = 0
for cont in range (1, 8):
    idade = int(input('Informe a sua idade: '))
    if idade >= 18:
        maioridade += 1
    elif idade < 18:
        menoridade += 1
print('{} já atingiram a maioridade, e {} ainda são menores de idade '.format(maioridade, menoridade))