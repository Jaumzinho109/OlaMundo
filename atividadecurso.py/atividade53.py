nome = str(input('Escreva seu nome: ')).strip().upper()
palavras = nome.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1 , -1, -1):
    inverso += junto[letra]
print(nome, ' ', inverso)