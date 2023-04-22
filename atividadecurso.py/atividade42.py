lado1 = int(input('Escreva o tamanho do primeiro segmento de reta: '))
lado2 = int(input('Agora, o segundo: '))
lado3 = int(input('Por fim, o terceiro: '))
if lado1 + lado2 > lado3 and lado3 + lado2 > lado1 and lado1 + lado3 > lado2:
    print('Então é possível formar um triângulo.')
    if lado1 == lado2 and lado2 == lado3:
        print('E ele é equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('E ele é isósceles.')
    else:
        print('E ele é escaleno')
else:
    print('Não é possível formar um triângulo')