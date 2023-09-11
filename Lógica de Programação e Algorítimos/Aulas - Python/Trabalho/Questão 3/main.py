def cachorroPeso(): # Início da função cachorroPeso() 
    while True:
        try: # Tentando executar o código abaixo
            print('\n', '-' * 28, 'PASSO (1/3)', '-' * 28, '\n')
            peso = int(input('Qual o peso do cachorro?: ')) # Variável que armazena o peso do cachorro
            if (peso < 3):
                return 40 # Retorna o valor 40
            elif (peso >= 3) and (peso < 10):
                return 50 # Retorna o valor 50
            elif (peso >= 10) and (peso < 30):
                return 60 # Retorna o valor 60
            elif (peso >= 30) and (peso < 50):
                return 70 # Retorna o valor 70
            elif (peso >= 50): # Verifica se o peso é maior ou igual a 50
                print('Não aceitamos cachorros tão pesados!')
                continue # Retorna para o início do while True
        except ValueError: # Caso o usuário digite qualquer outra coisa que não seja um valor aceito, mostrará um erro
            print('Erro: Insira um número válido para o peso!')
            print('Por favor, entre com o peso do cachorro novamente.')

def cachorroPelo(): # Início da função cachorroPelo() 
    while True:
        print('\n', '-' * 28, 'PASSO (2/3)', '-' * 28, '\n')
        print('[C] - Curto\n' +
              '[M] - Médio\n' +
              '[G] - Grande')
        pelo = input('Qual o pelo do cachorro?: ') # Variável que armazena o pelo do cachorro
        pelo = pelo.upper() # Faz com que a entrada do usuário seja transformada em maiuscula
        pelo = pelo.strip() # Remove os espaços adicionados pelo usuário 
        if (pelo == 'C'):
            return 1 # Retorna o valor 1
        elif (pelo == 'M'):
            return 1.5 # Retorna o valor 1.5
        elif (pelo == 'G'):
            return 2 # Retorna o valor 2
        elif (pelo != 'C') and (pelo != 'M') and (pelo != 'G'): # Verifica se a entrada do usuário é diferente das entradas que foram definidas
            print('Opção inválida! Tente novamente.')
            continue # Caso o usuário digite algo errado, retorna para o início do while True
        else:
            break
# Fim da função cachorroPelo() 
    
def cachorroExtra(): # Início da função cachorroExtra()
    acumulador = 0
    while True:
        print('\n', '-' * 28, 'PASSO (3/3)', '-' * 28, '\n')
        print('Gostaria de algum serviço adicional?' +
              '\n' +
              '[1] - Corte de Unhas | R$ 10.00\n' +
              '[2] - Escovar Dentes | R$ 12.00\n' +
              '[3] - Limpeza de Orelhas | R$ 15.00\n' +
              '[0] - Não desejo mais nenhum serviço\n')
        pedidoExtra = input('digite aqui a sua opção: ')
        if (pedidoExtra == '1'):
            acumulador += 10 # Pega o valor que está no acumulador e soma com 10
            continue # Caso o usuário digite algo errado, retorna para o início do while True
        elif (pedidoExtra == '2'):
            acumulador += 12 # Pega o valor que está no acumulador e soma com 12
            continue # Caso o usuário digite algo errado, retorna para o início do while True
        elif (pedidoExtra == '3'):
            acumulador += 15 # Pega o valor que está no acumulador e soma com 15
            continue # Caso o usuário digite algo errado, retorna para o início do while True
        elif (pedidoExtra == '0'):
            return acumulador # Retorna o valor que está no acumulador
        else:
            print('Opção inválida! Tente novamente.\n')
            continue # Caso o usuário digite algo errado, retorna para o início do while True
# Fim da função cachorroExtra()
      
# Início do main
print('Bem-vindo(a) ao petshop Tio Patinhas! - Proprietário: (Kage Jinsei)')
peso = cachorroPeso() # Variável que recebe a função cachorroPeso
pelo = cachorroPelo() # Variável que recebe a função cachorroPelo
extra = cachorroExtra() # Variável que recebe a função cachorroExtra

valorTotal = (peso * pelo) + extra # Variável que faz a multiplicação e soma dos valores

# Fechando o pedido e mostrando os valores detalhado do pedido com formatação para duas casas decimais
print('\n', '-' * 17, 'FECHANDO PEDIDO', '-' * 17, '\n' + 
      '\n' +
      f'Valor de acordo ao peso do seu cachorro: R$ {peso:.2f}\n' +
      f'Valor multiplicado de a cordo com o pelo: {pelo:.2f}x\n' +
      f'Valor dos serviços adicionais: R$ {extra:.2f}\n' +
      f'Valor total a ser pago: {valorTotal:.2f}')