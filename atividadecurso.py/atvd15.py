import random

nome1 = str(input('Fala o nome do primeiro aluno: '))
nome2 = str(input('Fala o nome do segundo aluno: '))
nome3 = str(input('Fala o nome do terceiro aluno: '))
nome4 = str(input('Fala o nome do quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('O nome sorteado foi {}'.format(lista))