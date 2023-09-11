print('-' * 36 +
      '\nBem-vindo(a) a Kage Jinsei Store!\n' +
      '-' * 36
      )

valorProduto = float(input('Insira o valor do produto: R$ ')) # Variável que armazena o valor do produto
quantidadeProduto = int(input('Insira a quantidade de produtos: ')) # Variável que armazena a quantidade de produtos

if (quantidadeProduto < 200): # Se a quantidade de produtos não chegar a 200, não haverá desconto
    descontoProduto = 0 # Não existe desconto para essa quantidade (abaixo de 200)
elif (quantidadeProduto >= 200) and (quantidadeProduto < 1000): # Se a quantidade de produtos for maior ou igual a 200 e menor que 1000, haverá desconto
    descontoProduto = 0.05 # Variável que armazena o valor do desconto
    mostrarDesconto = "5%" # Variável que armazena o valor do desconto em porcentagem
elif (quantidadeProduto >= 1000) and (quantidadeProduto < 2000): # Se a quantidade de produtos for maior ou igual a 1000 e menor que 2000, haverá desconto
    descontoProduto = 0.10 # Variável que armazena o valor do desconto
    mostrarDesconto = "10%" # Variável que armazena o valor do desconto em porcentagem
else: # Valores maior ou igual a 2000 cairão nessa função e haverá desconto
    descontoProduto = 0.15 # Variável que armazena o valor do desconto
    mostrarDesconto = "15%" # Variável que armazena o valor do desconto em porcentagem

valorTotal = valorProduto * quantidadeProduto # Variável que armazena o valor total do pedido, fazendo a multiplicação do valor do produto com a quantidade de produtos
print(f'Valor do pedido SEM desconto: R$ {valorTotal:.2f}') # Mostrando na tela o valor do pedido sem desconto com formatação para duas casas decimais
valorTotalDesconto = valorTotal - (valorTotal * descontoProduto) # Variável que armazena o valor total do pedido com desconto (é feita a subtração do resultado da multiplicação)
if (quantidadeProduto >= 200): # Se a quantidade de produtos for maior ou igual a 200, o valor com desconto será mostrado na tela
    print(f'Valor do pedido COM desconto de {mostrarDesconto}: R$ {valorTotalDesconto:.2f}') # Mostrando na tela o valor do pedido com desconto (e quanto foi aplicado) com formatação para duas casas decimais