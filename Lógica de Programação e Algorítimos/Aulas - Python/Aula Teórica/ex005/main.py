print('Escolha a fruta que deseja comprar:')
print('1 - Tangerina')
print('2 - Abacate')
print('3 - Melancia')
produto = int(input('Digite o número do produto: '))
quantidade = int(input('Quantas unidades?: '))

if (produto == 1):
    pagar = quantidade * 2.50
    print(f'Você comprou {quantidade} tangerinas. Valor a pagar: R$ {pagar}.')
elif (produto == 2):
    pagar = quantidade * 5.00
    print(f'Você comprou {quantidade} abacates. Valor a pagar: R$ {pagar}.')

elif (produto == 3):
    pagar = quantidade * 6.35
    print(f'Você comprou {quantidade} melancias. Valor a pagar: R$ {pagar}.')
else:
    print('Produto inexistente!')