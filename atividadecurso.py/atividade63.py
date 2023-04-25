termos = int(input('Informe a quantia de termos da sequência que você quer ver: '))
primeiro_termo = 0
segundo_termo = 1
print(primeiro_termo, ',', segundo_termo,end= ', ')
while termos > 0:
    termos = termos - 1
    seq_fib = (primeiro_termo + segundo_termo)
    print(seq_fib, end= ', ')
    primeiro_termo = segundo_termo
    segundo_termo = seq_fib

print('Fim')