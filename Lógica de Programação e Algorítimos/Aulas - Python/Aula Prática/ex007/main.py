print('--- CALCULADORA ---\n'
      '\n'
      '1 ou + | adição\n'
      '2 ou - | subtração\n'
      '3 ou * | multiplicação\n'
      '4 ou / | divisão\n'
      '0 - Encerrar Programa\n')

while True:
    operadores = input('Qual tipo de operação você deseja fazer?: ')
    if (operadores == '0'):
        print('Encerrando Programa...')
        break
    valor1 = int(input('Digite o primeiro: '))
    valor2 = int(input('Digite o segundo: '))

    if (operadores == '1') or (operadores == '+'):
        print(f'Resultado da adição: {valor1 + valor2}')
        continue
    elif (operadores == '2') or (operadores == '-'):
        print(f'Resultado da subtração: {valor1 - valor2}')
        continue
    elif (operadores == '3') or (operadores == '*'):
        print(f'Resultado da multiplicação:  {valor1 * valor2}')
        continue
    elif (operadores == '4') or (operadores == '/'):
        print(f'Resultado da divisão: {valor1 / valor2}')
        continue
    else:
        print('Operação Inválida!')
        continue