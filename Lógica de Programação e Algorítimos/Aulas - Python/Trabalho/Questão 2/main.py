print('Seja bem-vindo(a) a sorveteria IceCreamSandwich! (Proprietário: Kage Jinsei)')
print('Confira o nosso cardápio abaixo:')
print('-' *83)
print('| Nº DE BOLAS | SABOR TRADICIONAL (tr) | SABOR PREMIUM (pr) | SABOR ESPECIAL (es) |')
print('|      1      |        R$ 6,00         |      R$ 7,00       |       R$ 8,00       |')
print('|      2      |        R$ 11,00        |      R$ 13,00      |       R$ 15,00      |')
print('|      3      |        R$ 15,00        |      R$ 18,00      |       R$ 21,00      |')
print('-' * 83)

acumulador = 0

while True:
  saborSorvete = input('\nQual sabor de sorvete deseja? (tr/pr/es): ') # Pergunta qual sabor do pedido e armazena na variável
  saborSorvete = saborSorvete.lower() # Faz com que a entrada do usuário seja transformada em minuscula
  if (saborSorvete != 'tr') and (saborSorvete != 'pr') and (saborSorvete != 'es'): # Verifica se a entrada do usuário é diferente das entradas que foram definidas
    print('Sabor invalido! Tente novamente\n')
    continue # Caso o usuário digite algo errado, retorna para o início do while True
  
  bolasSorvete = input('Entre com o número de bolas desejada (1/2/3): ')
  if (bolasSorvete != '1') and (bolasSorvete != '2') and (bolasSorvete != '3'): # Verifica se a entrada do usuário é diferente das entradas que foram definidas
    print('Quantidade inexistente! Tente novamente\n')
    continue # Caso o usuário digite algo errado, retorna para o início do while True

  if (bolasSorvete == '1') and (saborSorvete == 'tr'):
    print('Você escolheu 1 bola de sorvete de sabor TRADICIONAL: R$ 6.00') # Mostra o pedido do usuário
    acumulador = acumulador + 6 # Pega o valor do acumulador e soma com +6

  elif (bolasSorvete == '1') and (saborSorvete == 'pr'):
    print('Você escolheu 1 bola de sorvete de sabor PREMIUM: R$ 7.00') # Mostra o pedido do usuário
    acumulador = acumulador + 7 # Pega o valor do acumulador e soma com +7

  elif (bolasSorvete == '1') and (saborSorvete == 'es'):
    print('Você escolheu 1 bola de sorvete de sabor ESPECIAL: R$ 8.00') # Mostra o pedido do usuário
    acumulador = acumulador + 8 # Pega o valor do acumulador e soma com +8

  elif (bolasSorvete == '2') and (saborSorvete == 'tr'):
    print('Você escolheu 2 bola de sorvete de sabor TRADICIONAL: R$ 11.00') # Mostra o pedido do usuário
    acumulador = acumulador + 11 # Pega o valor do acumulador e soma com +11

  elif (bolasSorvete == '2') and (saborSorvete == 'pr'):
    print('Você escolheu 2 bola de sorvete de sabor PREMIUM: R$ 13.00') # Mostra o pedido do usuário
    acumulador = acumulador + 13 # Pega o valor do acumulador e soma com +13
  
  elif (bolasSorvete == '2') and (saborSorvete == 'es'):
    print('Você escolheu 2 bola de sorvete de sabor ESPECIAL: R$ 15.00') # Mostra o pedido do usuário
    acumulador = acumulador + 15 # Pega o valor do acumulador e soma com +15

  elif (bolasSorvete == '3') and (saborSorvete == 'tr'):
    print('Você escolheu 3 bola de sorvete de sabor TRADICIONAL: R$ 15.00') # Mostra o pedido do usuário
    acumulador = acumulador + 15 # Pega o valor do acumulador e soma com +15

  elif (bolasSorvete == '3') and (saborSorvete == 'pr'):
    print('Você escolheu 3 bola de sorvete de sabor PREMIUM: R$ 18.00') # Mostra o pedido do usuário
    acumulador = acumulador + 18 # Pega o valor do acumulador e soma com +18

  elif (bolasSorvete == '3') and (saborSorvete == 'es'):
    print('Você escolheu 3 bola de sorvete de sabor ESPECIAL: R$ 21.00') # Mostra o pedido do usuário
    acumulador = acumulador + 21 # Pega o valor do acumulador e soma com +21

  outroPedido = input('Deseja fazer outro pedido? (S/N): ') # Pergunta se o usuário deseja fazer outro pedido e armazena na variável
  outroPedido = outroPedido.upper() # Faz com que a entrada do usuário seja transformada em maiuscula
  if (outroPedido == 'S'):
    continue # Caso o usuário queira outro pedido, retorna para o início do while True
  else:
    print(f'\nO valor total a ser pago é: R$ {acumulador:.2f}') # Mostra o valor total a ser pago com formatação para duas casas decimais
    break # Encerra o programa