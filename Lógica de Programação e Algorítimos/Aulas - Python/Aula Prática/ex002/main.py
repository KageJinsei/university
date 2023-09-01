km = int(input('Quantos Km foram percorridos com o veículo?: '))
dias = int(input('Por quantos dias o veículo foi alugado?: '))

preco = 60 * dias + 0.15 * km

print(f'Km rodados: {km}.\n Dias: {dias}')
print(f'Valor a ser pago: {preco}')