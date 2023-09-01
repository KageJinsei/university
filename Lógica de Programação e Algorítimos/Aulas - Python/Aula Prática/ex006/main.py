kwh = float(input('Quantos kWh foi consumido?: '))
tipo = input('Qual o tipo de instalação? (R, C ou I): ')

if (tipo == 'R'):
    if (kwh <= 500):
        preco = 0.40
    else:
        preco = 0.65
elif (tipo == 'C'):
    if (kwh <= 1000):
        preco = 0.55
    else:
        preco = 0.60
elif (tipo == 'I'):
    if (kwh <= 5000):
        preco = 0.55
    else:
        preco = 0.60

else:
    print('Instalação Inválida!')

print(f'Total a pagar: {kwh * preco}')