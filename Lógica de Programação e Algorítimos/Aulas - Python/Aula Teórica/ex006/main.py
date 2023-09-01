nome = input('Qual é o seu nome?: ')
idade = int(input('Qual é a sua idade?: '))

if (nome == 'Kage'):
    print('Olá, Kage!')
elif (idade < 18):
    print('Você não é o Kage! E é menor de idade!')
elif (idade >= 100):
    print('Você provavelmente não existe (ou é o Silvio Santos)')