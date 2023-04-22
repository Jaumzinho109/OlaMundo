nota1 = float(input('Informe o valor da primeira nota: '))
nota2 = float(input('Agora, a segunda nota: '))
media = (nota1 + nota2)/2
if media < 5:
    print('Que pena, você está reprovado.')
elif media >= 5 and media < 6.9:
    print('Você está de recuperação, melhore!')
else:
    print('Parabéns, você passou.')