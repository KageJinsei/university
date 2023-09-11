soma = 0
contador = 1

while (contador <= 5):
    x = float(input(f'Digite a {contador}ª nota: '))
    soma += x
    contador += 1
    media = soma / 5
print(f'Média final: {media}')