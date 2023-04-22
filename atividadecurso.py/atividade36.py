#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
#  e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

emprestimo = float(input('Qual o valor do empréstimo que você quer? '))
salario = float(input('Ok, agora me diga quantos você ganha de salário: '))
anos = int(input('Em quantos anos você vai pagar? '))
if emprestimo <= 0.3 * salario * anos * 12:
    print('Parabéns, o seu empréstimo foi aceito pelo banco.')
else:
    print('Desculpe, mas o seu pedido de empréstimo foi recusado.')