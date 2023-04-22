peso = float(input('Escreva a sua massa corporal em kg: '))
altura = float(input('Agora, a sua altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Então, você está abaixo do peso ideal.')
elif imc <= 25 and imc >= 18.5:
    print('Então, você está com o peso ideal.')
elif imc <= 30 and imc > 25:
    print('Então, você está em situação de sobrepeso.')
elif imc <= 40 and imc > 30:
    print('Então, você está obeso.')
else:
    print('Então, você está em situação de obesidade mórbida. ')
