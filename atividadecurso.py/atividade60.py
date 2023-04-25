from math import factorial
n = int(input('Digite um número inteiro para saber o valor do seu fatorial: '))
f = factorial(n)
while n > 0:
    print(n, ' x ', end= ' ')
    n = n -1
print('= ',f)

