preco = float(input('Digite o preço do protudo: R$ '))
percentual = float(input('Digite o percentual de desconto (ex: 0-100%): '))

desconto = preco * (percentual / 100)
precoFinal = preco - desconto

print(f'O preço do produto é de R$ {preco}. O desconto é de {percentual}%')
print(f'Valor do desconto: R$ {desconto}. Valor final do produto: R$ {precoFinal}.')
