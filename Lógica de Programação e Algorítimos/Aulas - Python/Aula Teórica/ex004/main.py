print('Escolha a fruta que deseja comprar:')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Digite o número do produto: '))
quantidade = int(input('Quantas unidades?: '))

if (produto == 1):
    pagar = quantidade * 2.30
    print(f'Você comprou {quantidade} maçãs. Valor a pagar: R$ {pagar}.')
else:
    if (produto == 2):
        pagar = quantidade * 3.60
        print(f'Você comprou {quantidade} laranjas. Valor a pagar: R$ {pagar}.')
    else:
        if (produto == 3):
            pagar = quantidade * 1.85
            print(f'Você comprou {quantidade} bananas. Valor a pagar: R$ {pagar}.')
        else:
            print('Produto inexistente!')