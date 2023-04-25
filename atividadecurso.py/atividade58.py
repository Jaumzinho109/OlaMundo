from random import randint
acertou = False
computador = randint(0, 10)
print('Tente adivinhar em qual número inteiro entre 0 e 10 eu pensei')
while not acertou:
    jogador = int(input('Digite um número inteiro: '))
    if jogador == computador:
        acertou = True
print('Acertou')
