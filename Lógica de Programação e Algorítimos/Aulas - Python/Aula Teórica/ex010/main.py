print('Digite uma mensagem que irei repetir para você!')
print('Para encerrar, escreva "sair".')

while True:
    texto = input('Digite: ')
    print(texto)
    if (texto == 'sair'):
        break
print('Encerrando o programa...')