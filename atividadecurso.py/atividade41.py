idade = int(input('Escreva a sua idade: '))
if idade < 10:
    print('Então, você está na classificação mirim de natação.')
elif idade < 15:
    print('Então, você está na classificação infantil de natação.')
elif idade < 20:
    print('Então, você está na classificação júnior de natação.')
elif idade < 26:
    print('Então, você está na classificação sênior de natação.')
else:
    print('Então, você está na classificação master de natação.')