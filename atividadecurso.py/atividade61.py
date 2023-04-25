primeiro_termo = float(input('Digite o primeiro termo da sua PA: '))
razao = float(input('Digite a razão da sua PA: '))
c = 9
soma = primeiro_termo
print(soma, end= ', ')
while c > 0:
    c = c - 1
    soma += razao
    print(soma, end= ', ')
