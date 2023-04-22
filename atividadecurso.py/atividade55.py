maior = 0
menor = 100000
for cont in range (1, 6):
    peso = float(input('Qual é o seu peso em kg '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O menor peso foi de {} kg, enquanto o maior foi {} kg'.format(menor, maior))