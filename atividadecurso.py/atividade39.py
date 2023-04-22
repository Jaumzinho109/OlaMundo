idade = int(input('Infome a sua idade: '))
if idade == 18:
    print('Então essa é a hora certa para você se alistar.')
elif idade > 18:
    print('Então você já se passou {} ano(s) do seu alistamento.'.format(idade - 18))
else:
    print('Então, ainda não chegou a hora do seu alistamento e ainda falta(m) {} ano(s) para que ele aconteça.'.format(18 - idade))