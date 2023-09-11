soma = 0
quantidade = 0

for i in range(1, 101):
    if (i % 2 == 0):
        soma += i
        quantidade += i
media = soma / quantidade
print(f'A média dos pares de 1 até 100 é: {media}.')        
