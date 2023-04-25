primeiro_termo = float(input('Digite o primeiro termo da sua PA: '))
razao = float(input('Digite a razão da sua PA: '))
c = int(input('Quantos termos você quer na sua PA?'))
soma = primeiro_termo
while c > 0:
    if c != 0:
        print(soma, end= ', ')
    c = c - 1
    soma += razao

print('Fim')

