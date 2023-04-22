razao = int(input('Informe um valor inteiro para ser a razão: '))
termo1 = int(input('Qual é o primeiro termo: '))
pa = 0
print(termo1, end= ' ')
for c in range (1, 11):
    if c == 1:
        pa = termo1
    pa = pa + razao
    print(pa, end = ' ')