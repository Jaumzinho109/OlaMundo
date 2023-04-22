#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#  No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
maior_idade = 0
older_name = ''
mulher_menos20 = 0
for cont in range (1,5):
    nome = str(input('Qual é o seu nome? '))
    idade = int(input('Qual é a sua idade? '))
    sexo = str(input('Qual é o seu sexo ? [M/F]'))
    soma += idade
    if idade < 20 and sexo == "F":
        mulher_menos20 += 1
    if idade > maior_idade and sexo == "M":
        older_name = nome
print('A média de idade é igual a {}'.format(soma/4))
print('O nome do homem mais velho é {}'.format(older_name))
print('{} mulhere(s) possuem menos de 20 anos'.format(mulher_menos20))
